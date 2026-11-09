#!/usr/bin/env python3
"""Record and verify integrity of an authorized local historical chat export.

The manifest does not contain conversation text. It is NOT proof that the
export is complete or that any historical claim is true.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


def inspect_text(path: Path) -> dict[str, object]:
    if not path.is_file():
        raise ValueError(f"Not a regular file: {path}")
    raw = path.read_bytes()
    if not raw or not raw.strip():
        raise ValueError("Input is empty or only whitespace")
    try:
        content = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError("Input is not UTF-8 text") from exc
    return {
        "sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": len(raw),
        "line_count": len(content.splitlines()),
    }


def check_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("A public HTTPS source URL is required")
    return url


def register(source: Path, source_url: str, manifest: Path) -> None:
    metrics = inspect_text(source)
    check_url(source_url)
    if manifest.exists():
        raise ValueError(f"Refusing to overwrite existing manifest: {manifest}")
    if manifest.resolve() == source.resolve():
        raise ValueError("Manifest path cannot equal source path")
    data = {
        "schema_version": "1.0",
        "source_id": "SRC-" + str(metrics["sha256"])[:16],
        "source_url": source_url,
        "source_basename": source.name,
        "registered_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sha256": metrics["sha256"],
        "size_bytes": metrics["size_bytes"],
        "line_count": metrics["line_count"],
        "completeness_reviewed": False,
        "historical_claims_reviewed": False,
        "event_identity": None,
        "state": "CAPTURED_UNREVIEWED",
        "note": "Hash verification only; source completeness, authorship and factual claims remain unverified.",
    }
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("x", encoding="utf-8") as out:
        json.dump(data, out, ensure_ascii=False, indent=2)
        out.write("\n")
    print(f"REGISTERED {data['source_id']} bytes={metrics['size_bytes']} manifest={manifest}")
    print("REVIEW REQUIRED: export coverage, event identity, references, and permission to publish")


def verify(source: Path, manifest: Path) -> None:
    metrics = inspect_text(source)
    if not manifest.is_file():
        raise ValueError(f"Manifest missing: {manifest}")
    data = json.loads(manifest.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != "1.0":
        raise ValueError("Invalid manifest schema")
    check_url(str(data.get("source_url", "")))
    expected_id = "SRC-" + str(metrics["sha256"])[:16]
    for key, expected in {**metrics, "source_id": expected_id}.items():
        if data.get(key) != expected:
            raise ValueError(f"Integrity mismatch: {key}, expected={data.get(key)!r}, actual={expected!r}")
    print(f"PASS integrity {expected_id}: bytes={metrics['size_bytes']}, lines={metrics['line_count']}")
    print("NOT VERIFIED: conversation coverage, historical truth, copyright/publication permissions")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    reg = sub.add_parser("register", help="Create a non-overwriting, text-free source manifest")
    reg.add_argument("--input", type=Path, required=True)
    reg.add_argument("--source-url", required=True)
    reg.add_argument("--output", type=Path, required=True)
    chk = sub.add_parser("verify", help="Check text bytes against a source manifest")
    chk.add_argument("--input", type=Path, required=True)
    chk.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "register":
            register(args.input, args.source_url, args.output)
        else:
            verify(args.input, args.manifest)
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
