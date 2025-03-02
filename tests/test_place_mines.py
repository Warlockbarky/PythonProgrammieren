import unittest
from source.minesweeper.place_mines import place_mines


class TestPlaceMines(unittest.TestCase):
    def setUp(self):
        self.rows, self.cols = 5, 5  # Field 5x5
        self.board = [
            [" ", "1", "2", "3", "4", "5"],
            ["1", "■", "■", "■", "■", "■"],
            ["2", "■", "■", "■", "■", "■"],
            ["3", "■", "■", "■", "■", "■"],
            ["4", "■", "■", "■", "■", "■"],
            ["5", "■", "■", "■", "■", "■"],
        ]

    def test_mines_placed_correctly(self):
        difficulty = 5  # Expect 5 mines
        updated_board = place_mines(self.board, self.rows, self.cols, difficulty)

        # Count the number of mines
        mine_count = sum(row.count("*") for row in updated_board)
        self.assertEqual(mine_count, difficulty, "The number of mines should match the difficulty")

        # Check that mines are placed only in closed cells
        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                if updated_board[r][c] == "*":
                    self.assertEqual(self.board[r][c], "■", "Mines should be placed only in closed cells")

    def test_no_more_mines_than_closed_cells(self):
        difficulty = 1  # Extremely high difficulty (1 mine per cell)
        updated_board = place_mines(self.board, self.rows, self.cols, difficulty)

        # The number of mines should not exceed the number of closed cells
        closed_cells = sum(row.count("■") for row in self.board)
        mine_count = sum(row.count("*") for row in updated_board)
        self.assertLessEqual(mine_count, closed_cells, "There cannot be more mines than closed cells")


if __name__ == "__main__":
    unittest.main()