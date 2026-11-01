#!/usr/bin/env python3
"""Source intake tests using real repository files, not invented history data."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "historical_source_intake.py"
SOURCE = ROOT / "README.md"
OTHER = ROOT / "AGENTS.md"
SOURCE_URL = "https://chatgpt.com/share/6ae6c57b-cd0c-83ee-9efb-96ec53e324af"


class SourceIntakeTests(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True, text=True, check=False,
        )

    def test_register_verify_and_reject_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as dirname:
            manifest = Path(dirname) / "manifest.json"
            registered = self.run_cli("register", "--input", str(SOURCE), "--source-url", SOURCE_URL,
                                      "--output", str(manifest))
            self.assertEqual(registered.returncode, 0, registered.stderr)
            data = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual(data["state"], "CAPTURED_UNREVIEWED")
            self.assertIsNone(data["event_identity"])
            self.assertFalse(data["completeness_reviewed"])
            self.assertFalse(data["historical_claims_reviewed"])
            self.assertNotIn(SOURCE.read_text(encoding="utf-8"), manifest.read_text(encoding="utf-8"))
            verified = self.run_cli("verify", "--input", str(SOURCE), "--manifest", str(manifest))
            self.assertEqual(verified.returncode, 0, verified.stderr)
            different = self.run_cli("verify", "--input", str(OTHER), "--manifest", str(manifest))
            self.assertNotEqual(different.returncode, 0)
            self.assertIn("Integrity mismatch", different.stderr)
            overwrite = self.run_cli("register", "--input", str(SOURCE), "--source-url", SOURCE_URL,
                                     "--output", str(manifest))
            self.assertNotEqual(overwrite.returncode, 0)
            self.assertIn("Refusing to overwrite", overwrite.stderr)

    def test_refuses_missing_source(self) -> None:
        with tempfile.TemporaryDirectory() as dirname:
            absent = Path(dirname) / "unavailable.md"
            manifest = Path(dirname) / "manifest.json"
            out = self.run_cli("register", "--input", str(absent), "--source-url", SOURCE_URL,
                               "--output", str(manifest))
            self.assertNotEqual(out.returncode, 0)
            self.assertFalse(manifest.exists())


if __name__ == "__main__":
    unittest.main()
