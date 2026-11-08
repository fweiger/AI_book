"""Read-only historical GAME-001 replay and outcome invariants.

Only original, GitHub-persisted comments/events are used; no synthetic chess positions.
"""
import json
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / "scripts"))
from game import COLUMNS, has_five, new_game, submit


class HistoricalReplayTests(unittest.TestCase):
    def test_all_31_comments_reproduce_final_board_and_rejection(self):
        saved = json.loads((BASE / "games/GAME-001/state.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["status"], "finished")
        self.assertEqual(saved["winner"], "white")
        self.assertEqual(saved["version"], 30)
        self.assertEqual(len(saved["moves"]), 30)
        self.assertEqual(len(saved["events"]), 31)
        self.assertEqual(len(saved["processed_comment_ids"]), 31)

        reconstructed = new_game(
            saved["game_id"], saved["issue_number"],
            saved["players"]["black"]["token"], saved["players"]["white"]["token"])
        for event in saved["events"]:
            side = event["side"]
            self.assertIn(side, ("black", "white"))
            token = saved["players"][side]["token"]
            body = f"MOVE {token} {event['coord']}"
            reconstructed = submit(reconstructed, event["comment_id"], body, event["author"])
            self.assertEqual(reconstructed["events"][-1], event)

        self.assertEqual(reconstructed, saved)
        rejects = [e for e in saved["events"] if e["result"] != "accepted"]
        self.assertEqual(len(rejects), 1)
        self.assertEqual(rejects[0]["result"], "wrong-turn")
        self.assertEqual(rejects[0]["comment_id"], 6718204222)

    def test_white_five_is_exact_final_winning_chain(self):
        saved = json.loads((BASE / "games/GAME-001/state.json").read_text(encoding="utf-8"))
        for coord in ["F9", "G10", "H11", "I12", "J13"]:
            col, row = COLUMNS.index(coord[0]), int(coord[1:]) - 1
            self.assertEqual(saved["board"][row][col], 2, coord)
        x, y = COLUMNS.index("J"), 12
        self.assertTrue(has_five(saved["board"], y, x, 2))
        self.assertEqual(saved["moves"][-1]["coord"], "J13")


if __name__ == "__main__":
    unittest.main()
