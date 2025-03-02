import unittest
from unittest.mock import patch
from source.minesweeper.print_board import print_board  # Ensure the path is correct
from colorama import Fore, Style

class TestPrintBoard(unittest.TestCase):
    def setUp(self):
        # Initialize the test board
        self.board = [
            [" ", "1", "2", "3"],
            ["1", "1", "2", "3"],
            ["2", "3", "4", "5"],
            ["3", "6", "7", "8"]
        ]

    @patch('builtins.print')
    def test_print_board(self, mock_print):
        # Call the function that should print the board
        print_board(self.board)

        # Expected lines with color codes
        expected_calls = [
            ("  1 2 3",),  # First row (header) without color
            (f"1 {Fore.BLUE}1{Style.RESET_ALL} {Fore.GREEN}2{Style.RESET_ALL} {Fore.RED}3{Style.RESET_ALL}",),  # First column and numbers in the second row
            (f"2 {Fore.RED}3{Style.RESET_ALL} {Fore.CYAN}4{Style.RESET_ALL} {Fore.MAGENTA}5{Style.RESET_ALL}",),  # First column and numbers in the third row
            (f"3 {Fore.YELLOW}6{Style.RESET_ALL} {Fore.WHITE}7{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}8{Style.RESET_ALL}",)  # First column and numbers in the fourth row
        ]

        # Check that mock_print was called with the correct lines
        for expected_call in expected_calls:
            mock_print.assert_any_call(*expected_call)

if __name__ == "__main__":
    unittest.main()