from .animated_input import animated_input
from .animated_text import animated_text
from .clear_console import clear_console


def choose_difficulty():
    clear_console()
    animated_text("Choose difficulty level:")
    animated_text("1. Easy")
    animated_text("2. Medium")
    animated_text("3. Hard")
    animated_text("4. Impossible")

    while True:
        choice = animated_input("Enter the difficulty level number (or 'quit' to exit to the menu): ")
        if choice.lower() == 'quit':
            return None, None
        if choice == "1":
            return 30, 6
        elif choice == "2":
            return 25, 5
        elif choice == "3":
            return 20, 4
        elif choice == "4":
            return 10, 3
        else:
            animated_text("Invalid choice. Please try again.")
