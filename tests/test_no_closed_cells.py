import unittest
from source.minesweeper.no_closed_cells import no_closed_cells

class TestNoClosedCells(unittest.TestCase):
    def test_all_cells_open(self):
        board = [
            [" ", "1", "2"],
            ["1", " ", " "],
            ["2", "*", " "]
        ]
        self.assertTrue(no_closed_cells(board, 2, 2))  # All cells are open

    def test_some_closed_cells(self):
        board = [
            [" ", "1", "2"],
            ["1", "■", " "],
            ["2", "*", "■"]
        ]
        self.assertFalse(no_closed_cells(board, 2, 2))  # There are closed cells

    def test_all_cells_closed(self):
        board = [
            [" ", "1", "2"],
            ["1", "■", "■"],
            ["2", "■", "■"]
        ]
        self.assertFalse(no_closed_cells(board, 2, 2))  # All cells are closed

    def test_mixed_board(self):
        board = [
            [" ", "1", "2", "3"],
            ["1", " ", "*", "■"],
            ["2", "■", " ", "*"],
            ["3", "*", " ", " "]
        ]
        self.assertFalse(no_closed_cells(board, 3, 3))  # There is at least one closed cell

if __name__ == "__main__":
    unittest.main()