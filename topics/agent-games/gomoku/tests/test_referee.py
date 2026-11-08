"""Active-game referee routing and lifecycle tests; network mocked, no live moves."""
import base64
import copy
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from game import new_game, submit
import referee


class FakeAPI:
    def __init__(self, game=None, active=None, comment_entries=None):
        self.repo = "fweiger/AI_book"
        self.active_path = referee.ACTIVE_PATH
        self.state_path = "topics/agent-games/gomoku/games/GAME-002/state.json"
        self.files = {
            self.active_path: active or {
                "schema_version": 1,
                "active_game": {
                    "game_id": "GAME-002",
                    "issue_number": 99,
                    "state_path": self.state_path,
                },
                "last_completed": {"game_id": "GAME-001"},
            },
            self.state_path: game or new_game("GAME-002", 99, "BLACK-2", "WHITE-2"),
        }
        self.comment_entries = comment_entries or []
        self.writes = []
        self.issue_updates = []

    def request(self, method, path, payload=None):
        prefix = f"/repos/{self.repo}/"
        assert path.startswith(prefix), path
        suffix = path[len(prefix):]
        if method == "GET" and suffix.startswith("contents/"):
            file = suffix[len("contents/"):]
            if file not in self.files:
                raise AssertionError("wrong state file: " + file)
            data = json.dumps(self.files[file]).encode()
            return {"sha": f"sha-{len(self.writes)}", "content": base64.b64encode(data).decode()}
        if method == "GET" and suffix.startswith("issues/99/comments"):
            return copy.deepcopy(self.comment_entries)
        if method == "PUT" and suffix.startswith("contents/"):
            file = suffix[len("contents/"):]
            assert file in self.files, file
            self.files[file] = json.loads(base64.b64decode(payload["content"]))
            self.writes.append(file)
            return {"content": {"sha": "new-sha"}}
        if method == "PATCH" and suffix == "issues/99":
            self.issue_updates.append(payload["body"])
            return {"number": 99}
        raise AssertionError((method, path))

    def run(self, event_number=None):
        environment = {"GITHUB_REPOSITORY": self.repo, "GITHUB_EVENT_NAME": "schedule"}
        if event_number is not None:
            environment["GITHUB_EVENT_NAME"] = "issue_comment"
        with tempfile.TemporaryDirectory() as temp:
            if event_number is not None:
                event_path = Path(temp) / "event.json"
                event_path.write_text(json.dumps({"issue": {"number": event_number}}))
                environment["GITHUB_EVENT_PATH"] = str(event_path)
            with patch.dict(os.environ, environment, clear=True):
                with patch.object(referee, "request", side_effect=self.request):
                    return referee.run()


class RefereeV2Tests(unittest.TestCase):
    def test_no_active_game_does_not_modify_old_match(self):
        a = FakeAPI(active={"schema_version": 1, "active_game": None,
                            "last_completed": {"game_id": "GAME-001"}})
        a.run()
        self.assertEqual(a.writes, [])
        self.assertEqual(a.issue_updates, [])

    def test_issue_24_cannot_trigger_game_002(self):
        a = FakeAPI(comment_entries=[
            {"id": 2001, "body": "MOVE BLACK-2 H8", "user": {"login": "tester"}}])
        a.run(event_number=24)
        self.assertEqual(a.writes, [])
        self.assertEqual(a.issue_updates, [])

    def test_active_game_002_accepts_its_own_move(self):
        a = FakeAPI(comment_entries=[
            {"id": 2002, "body": "MOVE BLACK-2 H8", "user": {"login": "tester"}}])
        a.run(event_number=99)
        s = a.files[a.state_path]
        self.assertEqual(s["version"], 1)
        self.assertEqual(s["turn"], "white")
        self.assertEqual(s["moves"][0]["coord"], "H8")
        self.assertIn(a.state_path, a.writes)
        self.assertNotIn(a.active_path, a.writes)
        self.assertIn("GAME-002", a.issue_updates[0])

    def test_wrong_id_binding_fails_before_any_writes(self):
        a = FakeAPI(game=new_game("GAME-002", 24, "BLACK-2", "WHITE-2"))
        with self.assertRaisesRegex(RuntimeError, "不一致"):
            a.run(event_number=99)
        self.assertEqual(a.writes, [])

    def test_bad_path_binding_is_rejected(self):
        with self.assertRaisesRegex(RuntimeError, "非法"):
            referee.validated_active({
                "schema_version": 1,
                "active_game": {
                    "game_id": "GAME-002", "issue_number": 99,
                    "state_path": "topics/agent-games/gomoku/games/GAME-001/state.json",
                },
            })

    def test_finished_game_clears_registry_after_final_issue(self):
        state = new_game("GAME-002", 99, "BLACK-2", "WHITE-2")
        for i in range(4):
            state = submit(state, 400 + 2*i, f"MOVE BLACK-2 {chr(65+i)}1")
            state = submit(state, 401 + 2*i, f"MOVE WHITE-2 {chr(65+i)}2")
        a = FakeAPI(game=state, comment_entries=[
            {"id": 420, "body": "MOVE BLACK-2 E1", "user": {"login": "tester"}}])
        a.run(event_number=99)
        self.assertEqual(a.files[a.state_path]["winner"], "black")
        self.assertIsNone(a.files[a.active_path]["active_game"])
        self.assertEqual(a.files[a.active_path]["last_completed"]["version"], 9)
        self.assertEqual(a.writes, [a.state_path, a.active_path])
        self.assertEqual(len(a.issue_updates), 1)
        self.assertIn("已结束", a.issue_updates[0])


if __name__ == "__main__":
    unittest.main()
