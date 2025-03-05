"""Module to clear console."""

import os


def clear_console():
    """
    Clear the console screen.

    Uses 'cls' for Windows and 'clear' for Unix-based systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
