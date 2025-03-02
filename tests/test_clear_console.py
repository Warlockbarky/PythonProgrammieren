import unittest
import os
from unittest.mock import patch
from minesweeper.clear_console import clear_console  # Import the function to be tested

class TestClearConsole(unittest.TestCase):
    @patch('os.system')  # Mock os.system to avoid actually clearing the screen
    def test_clear_console(self, mock_system):
        # Call the function
        clear_console()
        
        # Check that the correct command was called to clear the screen
        if os.name == 'nt':
            mock_system.assert_called_once_with('cls')  # For Windows
        else:
            mock_system.assert_called_once_with('clear')  # For Unix-like systems

if __name__ == '__main__':
    unittest.main()