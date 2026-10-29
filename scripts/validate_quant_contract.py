#!/usr/bin/env python3
"""Validate the TOPIC-004 A-share data contract using only the Python standard library."""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "topics/quant-rsi-research-evolution/research/a-share-data-contract-v0.json"
EXPECTED_FREQUENCIES = {"daily", "minute", "tick"}
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

    errors = []
    missing = REQUIRED_TOP_LEVEL - set(contract)
    if missing:
        errors.append(f"missing top-level keys: {sorted(missing)}")

    sources = contract.get("data_sources", [])
    by_frequency = {}
    for source in sources:
        frequency = source.get("frequency")
        if frequency not in EXPECTED_FREQUENCIES:
            errors.append(f"unsupported frequency: {frequency!r}")
            continue
        if frequency in by_frequency:
            errors.append(f"duplicate source contract for frequency: {frequency}")
        by_frequency[frequency] = source
        seen_roles = set()
        for mapping in source.get("field_mappings", []):
            role = mapping.get("role")
            if not role:
                errors.append(f"{frequency}: field mapping without role")
            elif role in seen_roles:
                errors.append(f"{frequency}: duplicate field role {role}")
            seen_roles.add(role)
            if not isinstance(mapping.get("required"), bool):
                errors.append(f"{frequency}.{role}: required must be boolean")

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
        if not set(required_frequencies).issubset(EXPECTED_FREQUENCIES):
            errors.append("required_frequencies contains an unsupported frequency")
        for frequency in required_frequencies:
            source = by_frequency.get(frequency)
            if source is None:
                errors.append(f"missing required source: {frequency}")
                continue
            for key in ("source_id", "source_version", "calendar_version", "universe_version", "raw_snapshot_hash"):
                if not source.get(key):
                    errors.append(f"{frequency}: {key} is required before freeze")
            for mapping in source.get("field_mappings", []):
                if mapping.get("required") and not mapping.get("source_field"):
                    errors.append(f"{frequency}.{mapping.get('role')}: required source_field is unresolved")
        task = contract.get("task_contract", {})
        for key in REQUIRED_LABEL_FIELDS:
            if not task.get(key):
                errors.append(f"task_contract.{key} is required before freeze")
        split = task.get("split", {})
        for key in ("train_start", "train_end", "valid_start", "valid_end", "outer_test_start", "outer_test_end",
                    "purge_sessions", "embargo_sessions"):
            if split.get(key) is None:
                errors.append(f"task_contract.split.{key} is required before freeze")
        execution = contract.get("execution_contract", {})
        for key in REQUIRED_EXECUTION_FIELDS:
            if execution.get(key) is None:
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
