#!/usr/bin/env python3
"""Validate the TOPIC-004 A-share data contract using only the Python standard library."""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "topics/quant-rsi-research-evolution/research/a-share-data-contract-v0.json"
EXPECTED_FREQUENCIES = {"daily", "minute", "tick"}
REQUIRED_ROLES = {
    "daily": {"symbol", "event_time", "available_at", "open", "high", "low", "close",
              "volume", "turnover", "price_adjustment_basis", "suspension_status",
              "limit_status", "universe_membership"},
    "minute": {"symbol", "bar_start_time", "bar_end_time", "available_at", "open",
               "high", "low", "close", "volume", "turnover"},
    "tick": {"symbol", "event_time", "receive_time", "available_at", "event_type"},
}
REQUIRED_GATES = {
    "source_field_semantics_verified", "point_in_time_available_at_verified",
    "raw_snapshot_hash_recorded", "historical_universe_verified",
    "label_boundary_purge_verified", "final_test_isolated_from_research_feedback",
    "execution_price_semantics_verified", "costs_slippage_and_capacity_verified",
    "replay_matches_live_data_availability", "evaluation_config_hash_frozen",
}


def is_blank(value):
    return value is None or (isinstance(value, str) and not value.strip())
REQUIRED_TOP_LEVEL = {
    "schema_version", "topic_id", "contract_id", "status", "required_frequencies",
    "data_sources", "task_contract", "execution_contract", "evaluation_gates",
    "formal_run_allowed", "unresolved_blockers",
}
REQUIRED_EXECUTION_FIELDS = {
    "fill_price_rule", "earliest_order_time_rule", "buy_cost_schedule",
    "sell_cost_schedule", "minimum_fee_rule", "stamp_duty_rule",
    "slippage_model", "market_impact_model", "volume_participation_cap",
    "historical_price_limit_rule", "suspension_and_untradable_rule",
    "t_plus_one_sell_rule",
}
REQUIRED_LABEL_FIELDS = {
    "target_expression", "signal_time_rule", "entry_time_rule", "exit_time_rule",
    "label_available_at_rule",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--strict", action="store_true",
                        help="fail unless the contract is frozen and all formal-run gates are satisfied")
    args = parser.parse_args()

    try:
        contract = json.loads(args.contract.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read valid JSON contract: {exc}", file=sys.stderr)
        return 1

    if not isinstance(contract, dict):
        print("ERROR: contract root must be a JSON object", file=sys.stderr)
        return 1

    errors = []
    missing = REQUIRED_TOP_LEVEL - set(contract)
    if missing:
        errors.append(f"missing top-level keys: {sorted(missing)}")

    sources = contract.get("data_sources", [])
    if not isinstance(sources, list):
        print("ERROR: data_sources must be a list", file=sys.stderr)
        return 1
    by_frequency = {}
    for source in sources:
        if not isinstance(source, dict):
            errors.append("each data_sources item must be an object")
            continue
        frequency = source.get("frequency")
        if frequency not in EXPECTED_FREQUENCIES:
            errors.append(f"unsupported frequency: {frequency!r}")
            continue
        if frequency in by_frequency:
            errors.append(f"duplicate source contract for frequency: {frequency}")
        by_frequency[frequency] = source
        mappings = source.get("field_mappings", [])
        if not isinstance(mappings, list):
            errors.append(f"{frequency}.field_mappings must be a list")
            continue
        seen_roles = set()
        for mapping in mappings:
            if not isinstance(mapping, dict):
                errors.append(f"{frequency}: each field mapping must be an object")
                continue
            role = mapping.get("role")
            if not role:
                errors.append(f"{frequency}: field mapping without role")
            elif role in seen_roles:
                errors.append(f"{frequency}: duplicate field role {role}")
            seen_roles.add(role)
            if not isinstance(mapping.get("required"), bool):
                errors.append(f"{frequency}.{role}: required must be boolean")
            if is_blank(mapping.get("semantic_definition")):
                errors.append(f"{frequency}.{role}: semantic_definition must be non-empty")
        missing_roles = REQUIRED_ROLES[frequency] - seen_roles
        if missing_roles:
            errors.append(f"{frequency}: missing required field roles: {sorted(missing_roles)}")
        for role in REQUIRED_ROLES[frequency] & seen_roles:
            core = next((m for m in mappings if isinstance(m, dict) and m.get("role") == role), None)
            if core is not None and core.get("required") is not True:
                errors.append(f"{frequency}.{role}: required core role must have required=true")

    if set(by_frequency) != EXPECTED_FREQUENCIES:
        errors.append(f"frequency contracts must be exactly {sorted(EXPECTED_FREQUENCIES)}")

    status = contract.get("status")
    blockers = contract.get("unresolved_blockers", [])
    if status == "BLOCKED_ON_DATA_CONTRACT":
        if not blockers:
            errors.append("blocked contract must list unresolved_blockers")
        if contract.get("formal_run_allowed") is not False:
            errors.append("blocked contract must set formal_run_allowed=false")
    elif status == "FROZEN":
        if blockers:
            errors.append("frozen contract cannot retain unresolved blockers")
        if contract.get("formal_run_allowed") is not True:
            errors.append("frozen contract must set formal_run_allowed=true")
        required_frequencies = contract.get("required_frequencies", [])
        if not required_frequencies:
            errors.append("frozen contract must name required_frequencies")
        if not isinstance(required_frequencies, list) or not required_frequencies:
            errors.append("frozen contract must name required_frequencies")
        elif any(x not in EXPECTED_FREQUENCIES for x in required_frequencies):
            errors.append("required_frequencies contains an unsupported frequency")
        elif len(required_frequencies) != len(set(required_frequencies)):
            errors.append("required_frequencies must not contain duplicates")

        gates = contract.get("evaluation_gates", {})
        if not isinstance(gates, dict) or set(gates) != REQUIRED_GATES:
            errors.append(f"evaluation_gates must contain exactly the required keys: {sorted(REQUIRED_GATES)}")
        for key in REQUIRED_GATES:
            if not isinstance(gates, dict) or gates.get(key) is not True:
                errors.append(f"evaluation gate not passed: {key}")

        for frequency in required_frequencies if isinstance(required_frequencies, list) else []:
            source = by_frequency.get(frequency)
            if source is None:
                errors.append(f"missing required source: {frequency}")
                continue
            for key in ("source_id", "source_version", "calendar_version", "universe_version", "raw_snapshot_hash"):
                if is_blank(source.get(key)):
                    errors.append(f"{frequency}: {key} is required before freeze")
            for mapping in source.get("field_mappings", []):
                if mapping.get("required") and is_blank(mapping.get("source_field")):
                    errors.append(f"{frequency}.{mapping.get('role')}: required source_field is unresolved")
                if mapping.get("required") and mapping.get("role") in {"open", "high", "low", "close", "volume", "turnover"} and is_blank(mapping.get("unit")):
                    errors.append(f"{frequency}.{mapping.get('role')}: unit is unresolved")
        task = contract.get("task_contract", {})
        if not isinstance(task, dict):
            errors.append("task_contract must be an object")
            task = {}
        if is_blank(task.get("task_family")):
            errors.append("task_contract.task_family is required before freeze")
        horizons = task.get("approved_horizons")
        if not isinstance(horizons, list) or not horizons or any(not isinstance(x, str) or not x.strip() for x in horizons):
            errors.append("task_contract.approved_horizons must be a non-empty list of strings")
        for key in REQUIRED_LABEL_FIELDS:
            if is_blank(task.get(key)):
                errors.append(f"task_contract.{key} is required before freeze")
        split = task.get("split", {})
        if not isinstance(split, dict):
            errors.append("task_contract.split must be an object")
            split = {}
        date_keys = ("train_start", "train_end", "valid_start", "valid_end", "outer_test_start", "outer_test_end")
        parsed_dates = {}
        for key in date_keys:
            value = split.get(key)
            if is_blank(value):
                errors.append(f"task_contract.split.{key} is required before freeze")
                continue
            try:
                parsed_dates[key] = date.fromisoformat(value)
            except (TypeError, ValueError):
                errors.append(f"task_contract.split.{key} must be an ISO date YYYY-MM-DD")
        if len(parsed_dates) == len(date_keys):
            ordered = [parsed_dates[key] for key in date_keys]
            if any(left >= right for left, right in zip(ordered, ordered[1:])):
                errors.append("train/valid/outer-test boundaries must be strictly chronological and non-overlapping")
        for key in ("purge_sessions", "embargo_sessions"):
            value = split.get(key)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                errors.append(f"task_contract.split.{key} must be a non-negative integer")
        execution = contract.get("execution_contract", {})
        if not isinstance(execution, dict):
            errors.append("execution_contract must be an object")
            execution = {}
        for key in REQUIRED_EXECUTION_FIELDS:
            if key not in execution or is_blank(execution.get(key)):
                errors.append(f"execution_contract.{key} is required before freeze")
        for key, value in contract.get("evaluation_gates", {}).items():
            if value is not True:
                errors.append(f"evaluation gate not passed: {key}")
    else:
        errors.append(f"unknown status: {status!r}")

    if args.strict and status != "FROZEN":
        errors.append("strict preflight requires status=FROZEN")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2 if args.strict else 1

    print(f"CONTRACT_STRUCTURE_OK contract_id={contract['contract_id']} status={status} "
          f"frequencies={len(by_frequency)} formal_run_allowed={contract['formal_run_allowed']}")
    if status != "FROZEN":
        print("FORMAL_RUN_BLOCKED: complete source mappings, time semantics, purge, execution costs, and gates first.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
