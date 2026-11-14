#!/usr/bin/env python3
"""Read-only AI_book index audit. GitHub is a data source, not an authority to edit INDEX.

Online: GITHUB_TOKEN=... python3 scripts/audit_topic_index.py --root . --repo fweiger/AI_book
Offline: python3 scripts/audit_topic_index.py --root . --fixture tests/fixture.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen

API = "https://api.github.com"
TOPIC = re.compile(r"TOPIC-(\d{3,})", re.I)
ROOT_DECL = re.compile(r"^\s*(?:\[TOPIC-(\d{3,})\]|TOPIC-(\d{3,}))", re.I)
GIT_URL = re.compile(r"https://github\.com/([\w.-]+)/([\w.-]+)/(issues|pull)/(\d+)")
MD_LINK = re.compile(r"\]\(([^)\n]+)\)")
VALID_REPO = re.compile(r"^[\w.-]+/[\w.-]+$")
IGNORE_CHILD_TAGS = re.compile(r"^\[(?:H\d+|DATA(?:-\d+)?|VIEW(?:-\d+)?|CASE-|R\d+|H\d+-DATA)", re.I)


class AuditFailure(RuntimeError):
    """Incomplete inputs: never report a clean audit on partial data."""


def github_json(url: str, token: str = "") -> object:
    if urlsplit(url).scheme != "https" or urlsplit(url).hostname != "api.github.com":
        raise AuditFailure(f"Blocked non-GitHub API URL: {url}")
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "ai-book-index-audit/1.0", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        with urlopen(Request(url, headers=headers), timeout=25) as response:
            if response.status != 200:
                raise AuditFailure(f"GitHub API HTTP {response.status}: {url}")
            return json.load(response)
    except (HTTPError, URLError, TimeoutError, ValueError, OSError) as exc:
        # Don't print exception response bodies (they may expose user data).
        raise AuditFailure(f"GitHub API fetch failed for {url}: {type(exc).__name__} {getattr(exc, 'code', '')}") from exc


def all_pages(path: str, token: str = "", getter=github_json, max_pages: int = 100) -> list[dict]:
    """An exact 100-item page is not proof that pagination ended."""
    items: list[dict] = []
    for page in range(1, max_pages + 1):
        separator = "&" if "?" in path else "?"
        url = f"{API}{path}{separator}per_page=100&page={page}"
        chunk = getter(url, token)
        if not isinstance(chunk, list) or any(not isinstance(item, dict) for item in chunk):
            raise AuditFailure(f"Invalid paginated payload at {url}")
        items.extend(chunk)
        if len(chunk) < 100:
            return items
    raise AuditFailure(f"Pagination exceeded {max_pages} pages for {path}; refusing incomplete results")


def snapshot(repo: str, token: str, getter=github_json) -> dict:
    if not VALID_REPO.fullmatch(repo):
        raise AuditFailure("Repository must have owner/repo form")
    base = f"/repos/{repo}"
    branch = getter(f"{API}{base}/branches/main", token)
    if not isinstance(branch, dict) or not isinstance(branch.get("commit"), dict):
        raise AuditFailure("Invalid main-branch metadata")
    head_sha = branch["commit"].get("sha")
    if not isinstance(head_sha, str) or not re.fullmatch("[0-9a-f]{40}", head_sha):
        raise AuditFailure("Missing/invalid main SHA")
    tree = getter(f"{API}{base}/git/trees/{head_sha}?recursive=1", token)
    if not isinstance(tree, dict) or tree.get("truncated") is not False or not isinstance(tree.get("tree"), list):
        raise AuditFailure("Git tree missing, invalid or truncated; refusing incomplete report")
    issues = all_pages(f"{base}/issues?state=all", token, getter)
    pulls = all_pages(f"{base}/pulls?state=all", token, getter)
    return {"main_sha": head_sha, "tree": tree["tree"],
            "issues": [x for x in issues if "pull_request" not in x], "pulls": pulls}


def classify_root(title: str) -> str | None:
    m = ROOT_DECL.search(title)
    if not m:
        return None
    tid = f"TOPIC-{m.group(1) or m.group(2)}"
    tail = title[m.end():].strip()
    if IGNORE_CHILD_TAGS.match(tail) or re.match(r"^[/｜:]\s*T\d+\b", tail, re.I):
        return None
    return tid


def index_main_ids(index: str) -> set[str]:
    section = index.split("## 一、已在 main 的专题", 1)
    if len(section) < 2:
        raise AuditFailure("INDEX.md lacks recognized 'main' topic section; update parser before using")
    part = section[1].split("\n## ", 1)[0]
    return {m.group(1) for line in part.splitlines() if (m := re.match(r"\|\s*(TOPIC-\d{3,})\s*\|", line))}


def migrated_ids(index: str) -> set[str]:
    # Explicit migration notice, not a generic mention of a moved project.
    return {f"TOPIC-{m.group(1)}" for line in index.splitlines()
            if "迁出" in line and "TOPIC-" in line
            for m in TOPIC.finditer(line)}


def linked_refs(index: str, repo: str) -> tuple[set[int], set[int]]:
    issues, pulls = set(), set()
    for owner, name, kind, number in GIT_URL.findall(index):
        if f"{owner}/{name}".lower() != repo.lower():
            continue
        (issues if kind == "issues" else pulls).add(int(number))
    return issues, pulls


def main_graphs(root: Path, tree: list[dict]) -> tuple[dict[str, list[str]], list[dict]]:
    found: dict[str, list[str]] = defaultdict(list)
    errors = []
    paths = sorted(x["path"] for x in tree if isinstance(x, dict) and isinstance(x.get("path"), str)
                   and re.fullmatch(r"topics/[^/]+/knowledge-graph\.json", x["path"]))
    for p in paths:
        f = root / p
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            tid = data.get("topic_id")
            if not isinstance(tid, str) or not re.fullmatch(r"TOPIC-\d{3,}", tid):
                raise ValueError("invalid topic_id")
            found[tid].append(p)
        except (OSError, ValueError, AttributeError) as exc:
            errors.append({"code": "main_graph_unreadable", "subject": p,
                           "detail": f"main graph cannot be parsed: {type(exc).__name__}"})
    return dict(found), errors


def broken_links(root: Path) -> list[dict]:
    warnings = []
    for md in sorted(root.rglob("*.md")):
        if any(part in {".git", ".venv", "node_modules", "dist", "site-packages"} for part in md.relative_to(root).parts):
            continue
        rel = md.relative_to(root).as_posix()
        try:
            content = md.read_text(encoding="utf-8")
        except OSError as exc:
            warnings.append({"code": "markdown_unreadable", "subject": rel, "detail": type(exc).__name__})
            continue
        for match in MD_LINK.finditer(content):
            raw = match.group(1).strip().split(' "', 1)[0]
            if raw.startswith(("https://", "http://", "mailto:", "#", "data:", "//")):
                continue
            target = unquote(raw.split("#", 1)[0].split("?", 1)[0]).strip("<>")
            if not target:
                continue
            path = (md.parent / target).resolve()
            if not path.is_relative_to(root.resolve()) or not path.exists():
                warnings.append({"code": "broken_local_link", "subject": rel, "detail": raw})
    return warnings


def audit(root: Path, repo: str, data: dict, index: str, check_links: bool = True) -> dict:
    if not VALID_REPO.fullmatch(repo):
        raise AuditFailure("Invalid repository name")
    for field in ("issues", "pulls", "tree"):
        if not isinstance(data.get(field), list):
            raise AuditFailure(f"Missing/invalid scan field: {field}")
    findings: list[dict] = []

    def finding(code: str, subject: str, detail: str, url: str = "") -> None:
        entry = {"code": code, "subject": subject, "detail": detail}
        if url:
            entry["url"] = url
        findings.append(entry)

    indexed_main = index_main_ids(index)
    migrated = migrated_ids(index)
    graph_map, graph_errors = main_graphs(root, data["tree"])
    for item in graph_errors:
        finding(**item)
    main_ids = set(graph_map)
    for tid in sorted(main_ids - indexed_main):
        finding("missing_main_topic", tid, f"Main graph not in main section: {', '.join(graph_map[tid])}")
    for tid in sorted(indexed_main - main_ids):
        finding("incorrect_main_claim", tid, "INDEX marks MAIN but no corresponding main graph exists")
    for tid, paths in sorted(graph_map.items()):
        if len(paths) > 1:
            finding("duplicate_main_topic_id", tid, ", ".join(paths))
    for tid in sorted(migrated & main_ids):
        finding("migrated_topic_reappeared", tid, "Topic marked migrated but graph appears again on main")

    issue_links, pr_links = linked_refs(index, repo)
    roots: dict[str, dict[str, list[dict]]] = defaultdict(lambda: {"issues": [], "pulls": []})
    for issue in data["issues"]:
        tid = classify_root(issue.get("title", ""))
        if not tid or tid in migrated:
            continue
        roots[tid]["issues"].append(issue)
        num = issue.get("number")
        if isinstance(num, int) and num not in issue_links:
            finding("missing_root_issue", tid, f"Top-level Issue #{num} not linked in INDEX",
                    f"https://github.com/{repo}/issues/{num}")

    for pr in data["pulls"]:
        num = pr.get("number")
        if not isinstance(num, int):
            raise AuditFailure("PR missing numeric number")
        tid = classify_root(pr.get("title", ""))
        merged = pr.get("merged_at") is not None
        if tid and tid not in migrated and not merged and pr.get("state") == "open":
            roots[tid]["pulls"].append(pr)
            if num not in pr_links:
                finding("missing_root_pr", tid, f"Open top-level PR #{num} absent from INDEX",
                        f"https://github.com/{repo}/pull/{num}")
        if num not in pr_links:
            continue
        # Only assert status when line contains status marker. Other prose can mention PR without status.
        target = f"https://github.com/{repo}/pull/{num}"
        contexts = [x.upper() for x in index.splitlines() if target in x]
        if merged and any("DRAFT PR" in x or "OPEN PR" in x for x in contexts):
            finding("stale_pr_state", f"PR #{num}", "PR is merged but INDEX still calls it open/draft", target)
        if pr.get("state") == "closed" and not merged and any("DRAFT PR" in x or "OPEN PR" in x for x in contexts):
            finding("stale_pr_state", f"PR #{num}", "PR is closed unmerged but INDEX still calls it open/draft", target)
        if pr.get("state") == "open" and not pr.get("draft") and any("DRAFT PR" in x for x in contexts):
            finding("stale_pr_state", f"PR #{num}", "PR is ready for review but INDEX marks draft", target)

    for tid, entries in sorted(roots.items()):
        issue_count = len(entries["issues"])
        # Multiple root PR branches may represent competing projects. This is a *candidate* collision.
        pr_count = len(entries["pulls"])
        if issue_count > 1 or pr_count > 1:
            ids = [f"issue#{x.get('number')}" for x in entries["issues"]]
            ids += [f"PR#{x.get('number')}" for x in entries["pulls"]]
            finding("possible_topic_id_collision", tid,
                    f"More than one root declaration (manual review only): {', '.join(ids)}")

    if check_links:
        for entry in broken_links(root):
            finding(**entry)

    findings.sort(key=lambda x: (x["code"], x["subject"], x["detail"]))
    return {"schema_version": 1, "repo": repo, "main_sha": data.get("main_sha", "unknown"),
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "status": "attention" if findings else "clean",
            "counts": {"main_topics": len(main_ids), "issues": len(data["issues"]),
                       "pulls": len(data["pulls"]), "findings": len(findings)},
            "migrated_ids": sorted(migrated), "findings": findings}


def render_markdown(report: dict) -> str:
    count = report["counts"]
    parts = ["# AI_book 索引漂移审计", "",
             f"- 状态：**{report['status'].upper()}**（仅结构/索引检查，不验证研究结论）",
             f"- 仓库：`{report['repo']}` · main SHA：`{report['main_sha']}`",
             f"- 审计时间（UTC）：{report['generated_at']}",
             f"- main 专题：{count['main_topics']} · Issues：{count['issues']} · PRs：{count['pulls']} · 待审核发现：{count['findings']}",
             "- 权限：**只读**；不会改写 INDEX、Issue、PR、迁移内容或实验结论。", "",
             "## 发现", ""]
    if not report["findings"]:
        parts.append("未发现本脚本规则覆盖范围内的索引漂移；不等于所有外部链接、研究证据都经过验证。")
    else:
        parts.append("| 类型 | 对象 | 说明与来源 |")
        parts.append("| --- | --- | --- |")
        for f in report["findings"]:
            link = f" ([来源]({f['url']}))" if f.get("url") else ""
            detail = f["detail"].replace("|", "\\|").replace("\n", " ")
            parts.append(f"| `{f['code']}` | `{f['subject']}` | {detail}{link} |")
    parts.extend(["", "## 审计边界", "",
                  "- GitHub Issues/PR 与 main 为不同证据层：研究入口不代表结论入库。",
                  "- `possible_topic_id_collision` 是人工核实线索，不自动重编号。",
                  "- 迁出专题仅保留迁出标记，不能把历史 PR 当成恢复内容的授权。",
                  "- 本地 Markdown 文件路径在 checkout 范围内检查；外部 HTTP 链接与历史分支文件未逐一验证。", ""])
    return "\n".join(parts)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--repo", default="fweiger/AI_book")
    parser.add_argument("--fixture", help="Offline JSON snapshot (no GitHub requests)")
    parser.add_argument("--out-dir", default="dist/index-audit")
    parser.add_argument("--no-local-links", action="store_true")
    options = parser.parse_args(argv)
    root = Path(options.root).resolve()
    out = Path(options.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    # An API failure must not leave yesterday's clean report looking like a fresh result.
    for filename in ("report.json", "report.md"):
        (out / filename).unlink(missing_ok=True)
    try:
        index = (root / "INDEX.md").read_text(encoding="utf-8")
        if options.fixture:
            data = json.loads(Path(options.fixture).read_text(encoding="utf-8"))
        else:
            data = snapshot(options.repo, os.environ.get("GITHUB_TOKEN", ""))
            try:
                local_sha = subprocess.check_output(
                    ["git", "-C", str(root), "rev-parse", "HEAD"],
                    text=True, stderr=subprocess.DEVNULL, timeout=8,
                ).strip()
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError) as exc:
                raise AuditFailure(f"Cannot confirm local Git HEAD: {type(exc).__name__}") from exc
            if local_sha != data["main_sha"]:
                raise AuditFailure("Checkout HEAD differs from current GitHub main; rerun on a fresh main checkout")
        result = audit(root, options.repo, data, index, check_links=not options.no_local_links)
        out.mkdir(parents=True, exist_ok=True)
        (out / "report.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (out / "report.md").write_text(render_markdown(result), encoding="utf-8")
        print(f"Index audit: {result['status']} ({result['counts']['findings']} findings)")
        return 0  # Findings need review; they do not block the read-only reporting job.
    except (AuditFailure, OSError, ValueError, TypeError, KeyError) as exc:
        print(f"AUDIT_INCOMPLETE: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2  # No fresh/clean report is written when data fetch/parse fails.


if __name__ == "__main__":
    raise SystemExit(main())
