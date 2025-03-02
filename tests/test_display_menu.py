import unittest
from unittest.mock import patch
from source.minesweeper.display_menu import display_menu

class TestDisplayMenu(unittest.TestCase):
    @patch("source.minesweeper.display_menu.clear_console")
    @patch("source.minesweeper.display_menu.animated_text")
    def test_display_menu(self, mock_animated_text, mock_clear_console):
        display_menu()

        # Check that clear_console was called exactly once
        mock_clear_console.assert_called_once()

        # Check that animated_text was called 3 times (1 header + 2 menu items)
        self.assertEqual(mock_animated_text.call_count, 3)

        # Check that animated_text was called with the correct arguments
        expected_calls = [
            ("Welcome to Minesweeper!",),
            ("1. Start Game",),
            ("2. Exit",),
        ]
        mock_animated_text.assert_has_calls([unittest.mock.call(*args) for args in expected_calls], any_order=False)

if __name__ == "__main__":
    unittest.main()