"""Offline deterministic tests; no credentials or GitHub network needed."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import audit_topic_index as a  # noqa: E402

REPO = "fweiger/AI_book"


def issue(n: int, title: str) -> dict:
    return {"number": n, "title": title, "state": "open"}


def pr(n: int, title: str, *, draft=True, state="open", merged_at=None) -> dict:
    return {"number": n, "title": title, "state": state, "draft": draft, "merged_at": merged_at}


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "topics/a").mkdir(parents=True)
        (self.root / "topics/a/knowledge-graph.json").write_text(json.dumps({"topic_id": "TOPIC-001"}))
        self.data = {"main_sha": "a" * 40, "tree": [{"path": "topics/a/knowledge-graph.json", "type": "blob"}],
                     "issues": [], "pulls": []}
        self.index = """# Index
## 一、已在 main 的专题
| ID | Title |
| --- | --- |
| TOPIC-001 | [A](topics/a/knowledge-graph.json) | MAIN |

## 二、持续研究：已有 Issue / PR，尚未入 main
"""

    def tearDown(self):
        self.tmp.cleanup()

    def scan(self, links=False):
        return a.audit(self.root, REPO, self.data, self.index, check_links=links)

    def codes(self, links=False):
        return [f["code"] for f in self.scan(links)["findings"]]

    def test_no_drifts(self):
        self.assertEqual(self.scan()["status"], "clean")

    def test_new_root_issue_is_discovered_and_child_is_ignored(self):
        self.data["issues"] = [issue(77, "[TOPIC-013][长期研究] 新专题"),
                               issue(78, "[TOPIC-011][H03] 下级分支")]
        self.assertEqual(self.codes().count("missing_root_issue"), 1)
        self.assertIn("/issues/77", self.scan()["findings"][0]["url"])

    def test_open_pr_missing_from_index(self):
        self.data["pulls"] = [pr(88, "[TOPIC-013] 新专题内容")]
        self.assertIn("missing_root_pr", self.codes())
        self.index += "\n[PR](https://github.com/fweiger/AI_book/pull/88) DRAFT PR\n"
        self.assertNotIn("missing_root_pr", self.codes())

    def test_pr_state_changes_are_detected(self):
        self.index += "\n| TOPIC-013 | [PR](https://github.com/fweiger/AI_book/pull/99) | DRAFT PR |\n"
        self.data["pulls"] = [pr(99, "[TOPIC-013] 研究版", draft=False)]
        self.assertIn("stale_pr_state", self.codes())
        self.data["pulls"] = [pr(99, "[TOPIC-013] 研究版", draft=False, state="closed", merged_at="2026-11-14T00:00Z")]
        self.assertIn("stale_pr_state", self.codes())

    def test_topic_id_collision_is_only_a_warning(self):
        self.data["pulls"] = [pr(2, "TOPIC-004: AI量化研究"),
                              pr(15, "TOPIC-004｜唐胥铁路"),
                              pr(17, "[TOPIC-004] 珍珠港")]
        self.index += "\n".join(f"[PR](https://github.com/{REPO}/pull/{n})" for n in (2,15,17))
        self.assertIn("possible_topic_id_collision", self.codes())
        self.assertEqual(self.scan()["status"], "attention")

    def test_migrated_topic_is_not_reintroduced(self):
        self.index += "\n**TOPIC-009 已迁出公开仓库，禁止恢复。**\n"
        self.data["issues"] = [issue(29, "[TOPIC-009] 睡眠研究")]
        self.data["pulls"] = [pr(59, "TOPIC-009 v0.3.2", state="closed", draft=False, merged_at="2026-11-14")]
        self.assertNotIn("missing_root_issue", self.codes())
        self.assertNotIn("missing_root_pr", self.codes())
        (self.root / "topics/sleep").mkdir()
        (self.root / "topics/sleep/knowledge-graph.json").write_text('{"topic_id":"TOPIC-009"}')
        self.data["tree"].append({"path": "topics/sleep/knowledge-graph.json", "type": "blob"})
        self.assertIn("migrated_topic_reappeared", self.codes())

    def test_new_main_and_false_main_are_caught(self):
        (self.root / "topics/b").mkdir()
        (self.root / "topics/b/knowledge-graph.json").write_text('{"topic_id":"TOPIC-016"}')
        self.data["tree"].append({"path": "topics/b/knowledge-graph.json", "type": "blob"})
        self.index += "\n| TOPIC-017 | Fake | MAIN |\n"  # outside main section; not asserted
        self.assertIn("missing_main_topic", self.codes())
        self.index = self.index.replace("| TOPIC-001", "| TOPIC-015")
        self.assertIn("incorrect_main_claim", self.codes())

    def test_local_relative_link_failure(self):
        (self.root / "README.md").write_text("[missing](topics/nonexistent.md)\n[valid](topics/a/knowledge-graph.json)")
        self.assertEqual(self.codes(links=True).count("broken_local_link"), 1)

    def test_missing_sections_fail_closed(self):
        with self.assertRaises(a.AuditFailure):
            a.audit(self.root, REPO, self.data, "# Old index", check_links=False)

    def test_missing_incomplete_api_data_fails_closed(self):
        broken = {"tree": [], "issues": []}
        with self.assertRaises(a.AuditFailure):
            a.audit(self.root, REPO, broken, self.index, check_links=False)
        def broken_getter(url, token):
            raise a.AuditFailure("HTTP 403")
        with self.assertRaises(a.AuditFailure):
            a.snapshot(REPO, "", getter=broken_getter)

    def test_pagination_and_truncation_detection(self):
        calls = []
        def fake(url, token):
            calls.append(url)
            return [{"number": k} for k in range(100)] if url.endswith("page=1") else [{"number": 101}]
        result = a.all_pages("/repos/fweiger/AI_book/issues?state=all", getter=fake)
        self.assertEqual(len(result), 101)
        self.assertEqual(len(calls), 2)
        def full(url, token):
            return [{}] * 100
        with self.assertRaises(a.AuditFailure):
            a.all_pages("/repos/x/y/issues", getter=full, max_pages=2)

    def test_snapshot_rejects_truncated_tree(self):
        def fake(url, token):
            if "/branches/main" in url:
                return {"commit": {"sha": "a" * 40}}
            if "/git/trees/" in url:
                return {"truncated": True, "tree": []}
            self.fail("Unexpected API request")
        with self.assertRaisesRegex(a.AuditFailure, "truncated"):
            a.snapshot(REPO, "", getter=fake)

    def test_cli_fixture_writes_report(self):
        self.data["issues"] = [issue(77, "[TOPIC-013] New project")]
        fixture = self.root / "fixture.json"
        fixture.write_text(json.dumps(self.data), encoding="utf-8")
        (self.root / "INDEX.md").write_text(self.index, encoding="utf-8")
        out = self.root / "dist/index-audit"
        self.assertEqual(a.main(["--root", str(self.root), "--fixture", str(fixture),
                                 "--out-dir", str(out), "--no-local-links"]), 0)
        result = json.loads((out / "report.json").read_text(encoding="utf-8"))
        self.assertEqual(result["status"], "attention")
        self.assertEqual(result["findings"][0]["code"], "missing_root_issue")
        self.assertIn("索引漂移审计", (out / "report.md").read_text(encoding="utf-8"))

    def test_failed_scan_removes_stale_report(self):
        (self.root / "INDEX.md").write_text(self.index, encoding="utf-8")
        out = self.root / "dist/index-audit"
        out.mkdir(parents=True)
        (out / "report.json").write_text('{"status":"clean"}')
        rc = a.main(["--root", str(self.root), "--fixture", str(self.root / "absent.json"),
                     "--out-dir", str(out), "--no-local-links"])
        self.assertEqual(rc, 2)
        self.assertFalse((out / "report.json").exists())

    def test_render_report_does_not_assert_claims(self):
        text = a.render_markdown(self.scan())
        self.assertIn("只读", text)
        self.assertIn("不验证研究结论", text)


if __name__ == "__main__":
    unittest.main()
