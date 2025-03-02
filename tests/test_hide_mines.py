import unittest
import copy
from source.minesweeper.hide_mines import hide_mines

class TestHideMines(unittest.TestCase):
    def test_hide_mines(self):
        board = [
            [" ", "1", "2", "3"],
            ["1", "■", "*", "■"],
            ["2", "*", "■", "*"],
            ["3", "■", "*", "■"]
        ]
        expected_board = [
            [" ", "1", "2", "3"],
            ["1", "■", "■", "■"],
            ["2", "■", "■", "■"],
            ["3", "■", "■", "■"]
        ]

        # Copy the board before calling the function to ensure the original does not change
        board_copy = copy.deepcopy(board)

        result = hide_mines(board, 3, 3)

        # Check that the result matches the expected board
        self.assertEqual(result, expected_board)

        # Check that the original board has not changed
        self.assertEqual(board, board_copy)

    def test_no_mines(self):
        board = [
            [" ", "1", "2"],
            ["1", "■", "■"],
            ["2", "■", "■"]
        ]
        expected_board = copy.deepcopy(board)  # The board without mines should not change

        result = hide_mines(board, 2, 2)

        # Check that the board remains unchanged
        self.assertEqual(result, expected_board)

if __name__ == "__main__":
    unittest.main()