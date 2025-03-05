"""Module providing an animated input function."""

from .animated_text import animated_text


def animated_input(prompt: str, delay: float = 0.01) -> str:
    """Display the prompt text with an animation effect and return user input.

    Args:
        prompt (str): The text to display before user input.
        delay (float, optional): The delay between characters. Default is 0.01.

    Returns:
        str: The user's input.
    """
    animated_text(prompt, delay)
    return input()
