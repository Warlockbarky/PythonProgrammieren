"""Module to choose difficulty level."""

from .animated_input import animated_input
from .animated_text import animated_text
from .clear_console import clear_console


def choose_difficulty() -> tuple[int | None, int | None]:
    """
    Clear the console and display the difficulty level options
    with animated text. Get the user's choice with an animated input prompt
    and return the corresponding settings.

    Returns:
        tuple: A tuple containing the settings for the chosen difficulty level.
               Returns (None, None) if the user chooses to quit.
    """
    clear_console()
    animated_text("Choose difficulty level:")
    animated_text("1. Easy")
    animated_text("2. Medium")
    animated_text("3. Hard")
    animated_text("4. Impossible")

    while True:
        choice = animated_input(
            "Enter the difficulty level number "
            "(or 'quit' to exit to the menu): "
            )
        if choice.lower() == 'quit':
            return None, None
        if choice == "1":
            return 30, 6
        if choice == "2":
            return 25, 5
        if choice == "3":
            return 20, 4
        if choice == "4":
            return 10, 3
        animated_text("Invalid choice. Please try again.")
