import unittest
from unittest.mock import patch
import sys
import os

# Add the path to the source folder to be able to import minesweeper
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))

from minesweeper.animated_input import animated_input  # Import the function to be tested

class TestAnimatedInput(unittest.TestCase):
    @patch('builtins.input', return_value='test_input')  # Mock input()
    @patch('minesweeper.animated_input.animated_text')  # Mock animated_text
    def test_animated_input(self, mock_animated_text, mock_input):
        result = animated_input("Enter something: ")
        self.assertEqual(result, 'test_input')  # Check that input() returned the expected value
        mock_animated_text.assert_called_once_with("Enter something: ", 0.01)  # Check the animation call

if __name__ == '__main__':
    unittest.main()