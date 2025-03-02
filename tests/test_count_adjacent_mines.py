import unittest
from minesweeper.count_adjacent_mines import count_adjacent_mines

class TestCountAdjacentMines(unittest.TestCase):

    def test_count_adjacent_mines(self):
        # Example board with several adjacent mines
        board = [
            [" ", "1", "2", "3"],  # Row indices start from 0
            ["1", "■", "*", "■"],
            ["2", "*", " ", " "],
            ["3", "*", " ", "■"],
            ["4", "*", " ", " "]
        ]
        rows = 4  # Number of rows
        cols = 3  # Number of columns
        expected_result = [
            [" ", "1", "2", "3"],  # Expected result
            ["1", "■", "*", "■"],
            ["2", "*", "3", "1"],
            ["3", "*", "3", "■"],
            ["4", "*", "2", " "]
        ]
        
        result = count_adjacent_mines(board, rows, cols)
        
        self.assertEqual(result, expected_result)

    def test_no_mines(self):
        # Example board with no mines
        board = [
            [" ", "1", "2", "3"],  # Row indices start from 0
            ["1", " ", " ", " "],
            ["2", " ", " ", " "],
            ["3", " ", " ", " "]
        ]
        rows = 3  # Number of rows
        cols = 3  # Number of columns
        expected_result = [
            [" ", "1", "2", "3"],  # Expected result
            ["1", " ", " ", " "],
            ["2", " ", " ", " "],
            ["3", " ", " ", " "]
        ]
        
        result = count_adjacent_mines(board, rows, cols)
        
        self.assertEqual(result, expected_result)

    def test_all_mines(self):
        # Example board where all cells contain mines
        board = [
            [" ", "1", "2", "3"],  # Row indices start from 0
            ["1", "*", "*", "*"],
            ["2", "*", "*", "*"],
            ["3", "*", "*", "*"]
        ]
        rows = 3  # Number of rows
        cols = 3  # Number of columns
        expected_result = [
            [" ", "1", "2", "3"],  # Expected result
            ["1", "*", "*", "*"],
            ["2", "*", "*", "*"],
            ["3", "*", "*", "*"]
        ]
        
        result = count_adjacent_mines(board, rows, cols)
        
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()