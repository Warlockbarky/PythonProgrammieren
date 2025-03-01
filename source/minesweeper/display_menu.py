from .clear_console import clear_console
from .animated_text import animated_text


def display_menu():
    clear_console()
    animated_text("Welcome to Minesweeper!")
    animated_text("1. Start Game")
    animated_text("2. Manage Profile")
    animated_text("3. View Records")
    animated_text("4. Exit")
