import unittest
import random
from source.minesweeper.open_cells import open_cells

class TestOpenCells(unittest.TestCase):
    def setUp(self):
        random.seed(42)  # Fix the seed for predictable tests

    def test_open_cells_easy_difficulty(self):
        board = [
            [" ", "1", "2", "3"],
            ["1", "■", "■", "■"],
            ["2", "■", "■", "■"],
            ["3", "■", "■", "■"]
        ]
        rows, cols = 3, 3
        difficulty = 20  # 20% of 9 cells ≈ 2 cells should open
        open_cells(board, rows, cols, 1, 1, difficulty)
        
        opened_count = sum(row.count(" ") for row in board)
        self.assertGreaterEqual(opened_count, 2)  # At least 2 cells are open
        self.assertLessEqual(opened_count, 3)  # Not too many cells are open

    def test_open_cells_medium_difficulty(self):
        board = [
            [" ", "1", "2", "3", "4"],
            ["1", "■", "■", "■", "■"],
            ["2", "■", "■", "■", "■"],
            ["3", "■", "■", "■", "■"],
            ["4", "■", "■", "■", "■"]
        ]
        rows, cols = 4, 4
        difficulty = 50  # 50% of 16 cells ≈ 8 cells should open
        open_cells(board, rows, cols, 2, 2, difficulty)

        opened_count = sum(row.count(" ") for row in board)
        self.assertGreaterEqual(opened_count, 8)  # At least 8 cells are open

    def test_no_open_outside_bounds(self):
        board = [
            [" ", "1", "2", "3"],
            ["1", "■", "■", "■"],
            ["2", "■", "■", "■"],
            ["3", "■", "■", "■"]
        ]
        rows, cols = 3, 3
        difficulty = 30
        open_cells(board, rows, cols, 2, 2, difficulty)  # Start in the center

        # Check that the top header row has not changed
        self.assertEqual(board[0], [" ", "1", "2", "3"])

        # Check that the row labels (first column) remain in place
        for r in range(1, rows + 1):
            self.assertEqual(board[r][0], str(r))

        # Check that there are no open cells on the borders (outside the game field)
        for row in range(1, rows + 1):
            self.assertNotIn(" ", board[row][0])  # Left border
            self.assertNotIn(" ", board[row][-1])  # Right border
        for col in range(1, cols + 1):
            self.assertNotIn(" ", board[0][col])  # Top border
            self.assertNotIn(" ", board[-1][col])  # Bottom border

if __name__ == "__main__":
    unittest.main()