import unittest
from unittest.mock import patch
import sys
import os

# Add the path to the source folder to import animated_text
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))

from minesweeper.animated_text import animated_text  # Import the function to be tested

class TestAnimatedText(unittest.TestCase):
    @patch('sys.stdout.write')  # Mock sys.stdout.write
    @patch('time.sleep')  # Mock time.sleep
    def test_animated_text(self, mock_sleep, mock_write):
        text = "Hello"
        delay = 0.01
        
        # Call the function
        animated_text(text, delay)
        
        # Check that sys.stdout.write was called 6 times (5 for characters + 1 for newline)
        self.assertEqual(mock_write.call_count, len(text) + 1)
        
        # Check that time.sleep was called 5 times (between each character, including the last one)
        self.assertEqual(mock_sleep.call_count, len(text))
        
        # Check that time.sleep was called with the correct argument
        mock_sleep.assert_called_with(delay)

if __name__ == '__main__':
    unittest.main()