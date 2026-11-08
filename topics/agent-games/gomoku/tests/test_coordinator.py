"""GAME-001 watcher tests: never let server make a move or start a model."""
import importlib.util
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / "scripts" / "coordinator.py"
spec = importlib.util.spec_from_file_location("gomoku_coordinator", SOURCE)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class CoordinatorTests(unittest.TestCase):
    def setUp(self):
        self.done_id = 6718199278   # real GAME-001 black H8 comment
        self.state = {
            "game_id": "GAME-001", "version": 3,
            "turn": "white", "status": "playing", "winner": None,
            "processed_comment_ids": [self.done_id],
        }
        self.pending_comment = {
            "id": 9876543210,
            "body": "MOVE GM001-W-87E01A58 H7",
            "created_at": "2026-11-08T06:25:00Z",
        }
        self.done_comment = {
            "id": self.done_id, "body": "MOVE GM001-B-35C14C40 H8",
            "created_at": "2026-11-08T06:20:00Z",
        }

    def test_only_unprocessed_move_requests_are_pending(self):
        comments = [self.done_comment, {"id": 7, "body": "hello"}, self.pending_comment]
        self.assertEqual(module.pending_moves(self.state, comments), [self.pending_comment])

    def test_grace_and_dispatch_cooldown(self):
        old = datetime(2026, 11, 8, 6, 25, tzinfo=timezone.utc).timestamp()
        self.assertFalse(module.should_dispatch(
            [self.pending_comment], {}, now=old + 20,
            grace_seconds=45, cooldown_seconds=180))
        self.assertTrue(module.should_dispatch(
            [self.pending_comment], {}, now=old + 50,
            grace_seconds=45, cooldown_seconds=180))
        import hashlib
        fingerprint = hashlib.sha256(str(self.pending_comment["id"]).encode()).hexdigest()
        self.assertFalse(module.should_dispatch(
            [self.pending_comment],
            {"fingerprint": fingerprint, "dispatched_at": old + 50},
            now=old + 70, grace_seconds=45, cooldown_seconds=180))
        self.assertTrue(module.should_dispatch(
            [self.pending_comment],
            {"fingerprint": fingerprint, "dispatched_at": old + 50},
            now=old + 250, grace_seconds=45, cooldown_seconds=180))

    def test_monitor_does_not_dispatch_or_submit_move(self):
        class FakeGitHub:
            def __init__(self, s, comments):
                self.s = s
                self.c = comments
                self.dispatches = 0
            def state(self):
                return self.s
            def comments(self):
                return self.c
            def dispatch_referee(self):
                self.dispatches += 1

        gh = FakeGitHub(self.state, [self.done_comment, self.pending_comment])
        with tempfile.TemporaryDirectory() as temp:
            cursor = {}
            result = module.run_once(
                gh, cursor, dispatch=False, grace_seconds=0,
                cooldown_seconds=60, cursor_path=Path(temp) / "cursor.json")
            self.assertEqual(result["turn"], "white")
            self.assertEqual(gh.dispatches, 0)
            self.assertEqual(self.state["version"], 3)
            self.assertEqual(self.state["processed_comment_ids"], [self.done_id])

    def test_no_model_or_move_submission_code(self):
        source = SOURCE.read_text(encoding="utf-8").lower()
        self.assertNotIn("subprocess", source)
        self.assertNotIn("codex", source)
        self.assertNotIn("def decide(", source)
        self.assertNotIn('def post(', source)


if __name__ == "__main__":
    unittest.main()
