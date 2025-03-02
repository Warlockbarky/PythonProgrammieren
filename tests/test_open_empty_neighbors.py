import unittest
from source.minesweeper.open_empty_neighbors import open_empty_neighbors


class TestOpenEmptyNeighbors(unittest.TestCase):
    def setUp(self):
        self.rows, self.cols = 5, 5  # Game field 5x5

        # Initial field with empty cells, mines (*), and closed cells (■)
        self.board = [
            [" ", "1", "2", "3", "4", "5"],
            ["1", "■", "■", "■", "■", "■"],
            ["2", "■", " ", " ", "■", "■"],  # Two empty cells in the center
            ["3", "■", " ", "■", "■", "■"],  # Another empty cell
            ["4", "■", "■", "■", "*", "■"],  # Mine at (4,4)
            ["5", "■", "■", "■", "■", "■"],
        ]

    def test_empty_neighbors_opening(self):
        updated_board = open_empty_neighbors(self.board, self.rows, self.cols)

        # Check that empty cells opened adjacent closed cells
        self.assertEqual(updated_board[2][1], " ")  # Left cell opened
        self.assertEqual(updated_board[3][1], " ")  # Bottom cell opened
        self.assertEqual(updated_board[3][2], " ")  # Adjacent cell opened

        # Check that the mine remained untouched
        self.assertEqual(updated_board[4][4], "*")

    def test_no_changes_for_full_board(self):
        full_board = [
            [" ", "1", "2", "3", "4", "5"],
            ["1", "1", "1", "2", "*", "1"],
            ["2", "1", "*", "3", "2", "1"],
            ["3", "1", "2", "*", "2", "1"],
            ["4", "1", "1", "2", "1", "1"],
            ["5", " ", " ", " ", "1", "*"],
        ]

        # After calling the function, it should not change anything as all cells are already open
        self.assertEqual(open_empty_neighbors(full_board, self.rows, self.cols), full_board)


if __name__ == "__main__":
    unittest.main()