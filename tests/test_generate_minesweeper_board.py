import unittest
from source.minesweeper.generate_minesweeper_board import generate_minesweeper_board

class TestGenerateMinesweeperBoard(unittest.TestCase):
    def test_board_dimensions(self):
        rows, cols = 5, 4
        board, board_rows, board_cols = generate_minesweeper_board(rows, cols)

        # Check that the correct number of rows and columns is returned
        self.assertEqual(board_rows, rows)
        self.assertEqual(board_cols, cols)

        # Header + rows rows = rows + 1
        self.assertEqual(len(board), rows + 1)
        # Header has cols + 1 columns (row number + columns)
        self.assertEqual(len(board[0]), cols + 1)

    def test_header_row(self):
        rows, cols = 3, 3
        board, _, _ = generate_minesweeper_board(rows, cols)

        # The first row should contain column numbers
        expected_header = [" "] + [str(i) for i in range(1, cols + 1)]
        self.assertEqual(board[0], expected_header)

    def test_row_labels_and_cells(self):
        rows, cols = 4, 4
        board, _, _ = generate_minesweeper_board(rows, cols)

        for i in range(1, rows + 1):  # Start from 1, as 0 is the header
            row_label = str(i).rjust(len(str(rows)))  # Row number with the required width
            self.assertEqual(board[i][0], row_label)
            self.assertEqual(board[i][1:], ["■"] * cols)  # Check that the cells are filled with "■"

if __name__ == "__main__":
    unittest.main()