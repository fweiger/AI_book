#!/usr/bin/env python3
"""Regression tests for the TOPIC-004 data-contract preflight."""

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "topics/quant-rsi-research-evolution/research/a-share-data-contract-v0.json"
VALIDATOR = ROOT / "scripts/validate_quant_contract.py"


class ContractValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))

    def run_contract(self, contract, strict=False):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "contract.json"
            path.write_text(json.dumps(contract), encoding="utf-8")
            command = [sys.executable, str(VALIDATOR), "--contract", str(path)]
            if strict:
                command.append("--strict")
            return subprocess.run(command, capture_output=True, text=True, check=False)

    def test_current_template_is_valid_but_formally_blocked(self):
        result = self.run_contract(copy.deepcopy(self.template))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("FORMAL_RUN_BLOCKED", result.stdout)

    def test_strict_mode_rejects_blocked_template(self):
        result = self.run_contract(copy.deepcopy(self.template), strict=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("strict preflight requires status=FROZEN", result.stderr)

    def test_missing_core_field_role_is_rejected(self):
        contract = copy.deepcopy(self.template)
        daily = next(source for source in contract["data_sources"] if source["frequency"] == "daily")
        daily["field_mappings"] = [
            mapping for mapping in daily["field_mappings"] if mapping["role"] != "available_at"
        ]
        result = self.run_contract(contract)
        self.assertEqual(result.returncode, 1)
        self.assertIn("daily: missing required field roles", result.stderr)

    def test_frozen_contract_cannot_bypass_unresolved_mappings(self):
        contract = copy.deepcopy(self.template)
        contract["status"] = "FROZEN"
        contract["required_frequencies"] = ["daily"]
        contract["unresolved_blockers"] = []
        contract["formal_run_allowed"] = True
        contract["evaluation_gates"] = {key: True for key in contract["evaluation_gates"]}
        result = self.run_contract(contract)
        self.assertEqual(result.returncode, 1)
        self.assertIn("source_id is required before freeze", result.stderr)
        self.assertIn("required source_field is unresolved", result.stderr)

    def test_non_object_json_root_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "contract.json"
            path.write_text("[]", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(VALIDATOR), "--contract", str(path)],
                capture_output=True, text=True, check=False,
            )
        self.assertEqual(result.returncode, 1)
        self.assertIn("contract root must be a JSON object", result.stderr)


if __name__ == "__main__":
    unittest.main()
