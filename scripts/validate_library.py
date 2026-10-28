#!/usr/bin/env python3
"""Validate local AI_book metadata and links without any third-party packages.

Run: python3 scripts/validate_library.py
This checks integrity and navigation, not whether a scholarly claim is true.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
ERRORS: list[str] = []
SEEN_BOOK_IDS: set[str] = set()
SEEN_TOPIC_IDS: set[str] = set()


def error(context: str, detail: str) -> None:
    ERRORS.append(f"{context}: {detail}")


def ensure_exists(path: Path, label: str) -> None:
    if not path.exists():
        error(label, "missing file " + str(path))


def check_book_cards() -> int:
    count = 0
    for path in sorted((ROOT / "library" / "books").glob("B[0-9][0-9][0-9]-*.md")):
        count += 1
        bid = path.name[:4]
        if bid in SEEN_BOOK_IDS:
            error(str(path), "duplicate book ID " + bid)
        SEEN_BOOK_IDS.add(bid)
        if bid not in path.read_text(encoding="utf-8"):
            error(str(path), "book ID not mentioned in content")
    return count


def check_graph(graph_path: Path) -> tuple[int, int]:
    name = graph_path.relative_to(ROOT).as_posix()
    try:
        data = json.loads(graph_path.read_text(encoding="utf-8"))
    except Exception as exc:
        error(name, "invalid JSON " + str(exc))
        return (0, 0)

    topic = data.get("topic_id")
    if not isinstance(topic, str) or not re.fullmatch(r"TOPIC-[0-9]{3,}", topic):
        error(name, "invalid topic_id")
    elif topic in SEEN_TOPIC_IDS:
        error(name, "duplicate topic_id " + topic)
    else:
        SEEN_TOPIC_IDS.add(topic)

    version = data.get("topic_version")
    if not isinstance(version, str) or not re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", version):
        error(name, "topic_version must be MAJOR.MINOR.PATCH")
    if data.get("schema_version") != "1.0":
        error(name, "expected schema_version 1.0")

    book_refs = data.get("books", [])
    related = data.get("related_books", [])
    b_ids: set[str] = set()
    for b in book_refs + related:
        bid = b.get("id")
        if not isinstance(bid, str) or bid in b_ids:
            error(name, "invalid/duplicate book ref " + str(bid))
        b_ids.add(bid)
        if bid not in SEEN_BOOK_IDS:
            error(name, "book ref missing book card " + str(bid))
        card = b.get("card")
        if isinstance(card, str):
            ensure_exists((graph_path.parent / card).resolve(), name)
        else:
            error(name, "book " + str(bid) + " lacks card path")

    nodes = data.get("nodes", [])
    node_ids: set[str] = set()
    for n in nodes:
        nid = n.get("id")
        if not isinstance(nid, str) or not nid or nid in node_ids:
            error(name, "invalid/duplicate node ID " + str(nid))
        node_ids.add(nid)
        book = n.get("book")
        if book is not None and book not in b_ids:
            error(name, "node " + str(nid) + " points to unlisted book " + str(book))
        card = n.get("book_card")
        if card:
            ensure_exists((graph_path.parent / card).resolve(), name)

    edges = data.get("edges", [])
    edge_ids: set[tuple[str, str, str]] = set()
    for e in edges:
        src, dst, rel = e.get("source"), e.get("target"), e.get("relation")
        if src not in node_ids or dst not in node_ids:
            error(name, "edge references unknown node " + str((src, dst)))
        if not isinstance(rel, str) or not rel.strip():
            error(name, "edge lacks relation")
        key = (str(src), str(dst), str(rel))
        if key in edge_ids:
            error(name, "duplicate edge " + str(key))
        edge_ids.add(key)

    for route in data.get("reading_paths", []):
        if not route.get("id"):
            error(name, "reading route without ID")
        for nid in route.get("nodes", []):
            if nid not in node_ids:
                error(name, "reading route points to unknown node " + str(nid))

    for required in ("README.md", "questions.md", "knowledge-map.md", "reading-path.md",
                     "claims.md", "CHANGELOG.md", "sessions/README.md"):
        ensure_exists(graph_path.parent / required, name)
    return len(nodes), len(edges)


def check_markdown_links() -> int:
    checked = 0
    pattern = re.compile(r"\]\(([^)\n]+)\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            uri = match.group(1).strip()
            if uri.startswith(("https://", "http://", "mailto:", "#", "data:")):
                continue
            uri = unquote(uri.split("#", 1)[0].split("?", 1)[0])
            if not uri or uri.startswith("//"):
                continue
            if uri.startswith("<") and uri.endswith(">"):
                uri = uri[1:-1]
            # Markdown link titles are not paths.
            uri = uri.split(' "', 1)[0]
            candidate = (path.parent / uri).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                error(path.relative_to(ROOT).as_posix(), "relative link escapes repository " + uri)
                continue
            checked += 1
            if not candidate.exists():
                error(path.relative_to(ROOT).as_posix(), "broken link " + uri)
    return checked


def main() -> int:
    for p in ("README.md", "INDEX.md", "WORKFLOW.md", "AGENTS.md", "VERSIONING.md"):
        ensure_exists(ROOT / p, "root")
    cards = check_book_cards()
    nodes = edges = 0
    graphs = list((ROOT / "topics").glob("*/knowledge-graph.json"))
    for graph in graphs:
        n, e = check_graph(graph)
        nodes += n
        edges += e
    index = (ROOT / "INDEX.md").read_text(encoding="utf-8")
    for tid in SEEN_TOPIC_IDS:
        if tid not in index:
            error("INDEX.md", "missing topic " + tid)
    links = check_markdown_links()

    print(f"books={cards} topics={len(graphs)} nodes={nodes} edges={edges} local_links_checked={links}")
    if ERRORS:
        for e in ERRORS:
            print("ERROR:", e, file=sys.stderr)
        return 1
    print("PASS: local knowledge-base structural validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
