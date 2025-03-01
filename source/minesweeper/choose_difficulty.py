from .animated_input import animated_input  # Import the animated_input function
from .animated_text import animated_text  # Import the animated_text function
from .clear_console import clear_console  # Import the clear_console function


def choose_difficulty():
    clear_console()  # Clear the console screen
    animated_text("Choose difficulty level:")  # Display the prompt for choosing difficulty
    animated_text("1. Easy")  # Display the Easy option
    animated_text("2. Medium")  # Display the Medium option
    animated_text("3. Hard")  # Display the Hard option
    animated_text("4. Impossible")  # Display the Impossible option

    while True:
        # Get the user's choice with an animated input prompt
        choice = animated_input("Enter the difficulty level number (or 'quit' to exit to the menu): ")
        if choice.lower() == 'quit':
            return None, None  # Exit if the user types 'quit'
        if choice == "1":
            return 30, 6  # Return settings for Easy difficulty
        elif choice == "2":
            return 25, 5  # Return settings for Medium difficulty
        elif choice == "3":
            return 20, 4  # Return settings for Hard difficulty
        elif choice == "4":
            return 10, 3  # Return settings for Impossible difficulty
        else:
            animated_text("Invalid choice. Please try again.")  # Prompt for a valid choice if input is invalid
