from .animated_text import animated_text  # Import the animated_text function from the animated_text module


def animated_input(prompt, delay=0.01):
    # Display the prompt text with an animation effect
    animated_text(prompt, delay)
    # Return the user's input after the animated prompt
    return input()
