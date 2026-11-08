"""五子棋自动裁判规则测试。"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
from game import board_text, has_five, new_game, parse_submission, submit, issue_body


class GameTest(unittest.TestCase):
    def setUp(self):
        self.s = new_game("GAME-001", 24, "BLACK-CODE", "WHITE-CODE")

    def test_empty_board_and_coordinate(self):
        self.assertEqual(self.s["board"][7][7], 0)
        self.assertEqual(parse_submission("MOVE BLACK-CODE H8"), ("BLACK-CODE", "H8"))
        self.assertIsNone(parse_submission("MOVE BLACK-CODE P8"))
        self.assertIsNone(parse_submission("MOVE BLACK-CODE H16"))
        self.assertIn("A B C D", board_text(self.s))

    def test_turn_and_duplicate(self):
        s = submit(self.s, 101, "MOVE BLACK-CODE H8", "shared")
        self.assertEqual(s["board"][7][7], 1)
        self.assertEqual(s["turn"], "white")
        self.assertEqual(submit(s, 101, "MOVE BLACK-CODE H8"), s)
        rejected = submit(s, 102, "MOVE BLACK-CODE G8")
        self.assertEqual(rejected["version"], 1)
        self.assertEqual(rejected["events"][-1]["result"], "wrong-turn")
        occupied = submit(rejected, 103, "MOVE WHITE-CODE H8")
        self.assertEqual(occupied["events"][-1]["result"], "occupied")
        next_s = submit(occupied, 104, "MOVE WHITE-CODE G8")
        self.assertEqual(next_s["board"][7][6], 2)
        self.assertEqual(next_s["turn"], "black")

    def test_unknown_token_and_non_move(self):
        self.assertEqual(submit(self.s, 7, "hello"), self.s)
        s = submit(self.s, 8, "MOVE WRONG H8")
        self.assertEqual(s["events"][-1]["result"], "unknown-token")

    def test_five_all_directions(self):
        for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
            b = [[0] * 15 for _ in range(15)]
            for i in range(5):
                b[7 + i * dr][7 + i * dc] = 1
            self.assertTrue(has_five(b, 7 + 4 * dr, 7 + 4 * dc, 1))

    def test_issue_body_dynamic_step_and_no_old_token(self):
        s = new_game("GAME-002", 99, "BLACK-NEW", "WHITE-NEW")
        url = "https://github.com/fweiger/AI_book/blob/main/GAME-002-state.json"
        initial = issue_body(s, url)
        self.assertIn("尚未落子（空棋盘）", initial)
        self.assertIn("第 1 手，黑方 AI-A", initial)
        self.assertNotIn("GM001-B", initial)
        s = submit(s, 1234, "MOVE BLACK-NEW H8")
        after = issue_body(s, url)
        self.assertIn("第 1 手，黑方 AI-A H8", after)
        self.assertIn("第 2 手，白方 AI-B", after)
        self.assertIn("BLACK-NEW", after)

    def test_finish(self):
        s = self.s
        for i in range(4):
            s = submit(s, 100 + i * 2, f"MOVE BLACK-CODE {chr(65+i)}1")
            s = submit(s, 101 + i * 2, f"MOVE WHITE-CODE {chr(65+i)}2")
        s = submit(s, 108, "MOVE BLACK-CODE E1")
        self.assertEqual((s["status"], s["winner"], s["turn"]), ("finished", "black", None))
        s = submit(s, 109, "MOVE WHITE-CODE E2")
        self.assertEqual(s["events"][-1]["result"], "game-finished")


if __name__ == "__main__":
    unittest.main()
