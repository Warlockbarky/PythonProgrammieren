"""Module to display menu."""

from .clear_console import clear_console
from .animated_text import animated_text


def display_menu():
    """
    Clear the console and display the main menu with animated text.
    """
    clear_console()
    animated_text("Welcome to Minesweeper!")
    animated_text("1. Start Game")
    animated_text("2. Exit")
