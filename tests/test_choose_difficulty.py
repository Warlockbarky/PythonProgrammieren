import unittest
from unittest.mock import patch

# Import the function to be tested
from minesweeper.choose_difficulty import choose_difficulty  # Specify the path to the file here

class TestChooseDifficulty(unittest.TestCase):
    @patch('minesweeper.choose_difficulty.animated_text')  # Mock the animated_text function
    @patch('minesweeper.choose_difficulty.animated_input')  # Mock the animated_input function
    @patch('minesweeper.choose_difficulty.clear_console')  # Mock the clear_console function
    def test_choose_difficulty(self, mock_clear, mock_input, mock_animated_text):
        # Preparation
        mock_input.return_value = "2"  # Substitute user input with "2" (medium level)

        # Call the function
        result = choose_difficulty()

        # Check that clear_console and animated_text were called the correct number of times
        self.assertEqual(mock_clear.call_count, 1)
        self.assertEqual(mock_animated_text.call_count, 5)  # 5 lines of text to display

        # Check that the correct settings were returned for the medium level
        self.assertEqual(result, (25, 5))

    @patch('minesweeper.choose_difficulty.animated_text')
    @patch('minesweeper.choose_difficulty.animated_input')
    @patch('minesweeper.choose_difficulty.clear_console')
    def test_invalid_input(self, mock_clear, mock_input, mock_animated_text):
        # Preparation
        mock_input.side_effect = ["5", "2"]  # First invalid input, then "2" (medium level)

        # Call the function
        result = choose_difficulty()

        # Check that an error message was printed for invalid input
        self.assertTrue(mock_animated_text.call_args_list[-1][0][0] == "Invalid choice. Please try again.")
        
        # Check that the correct settings were returned for the medium level
        self.assertEqual(result, (25, 5))

    @patch('minesweeper.choose_difficulty.animated_text')
    @patch('minesweeper.choose_difficulty.animated_input')
    @patch('minesweeper.choose_difficulty.clear_console')
    def test_quit_option(self, mock_clear, mock_input, mock_animated_text):
        # Preparation
        mock_input.return_value = "quit"  # User inputs 'quit'

        # Call the function
        result = choose_difficulty()

        # Check that the function returned None, None, indicating exit
        self.assertEqual(result, (None, None))

if __name__ == '__main__':
    unittest.main()