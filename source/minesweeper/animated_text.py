"""Module providing an animated text function."""

import sys
import time


def animated_text(text: str, delay: float = 0.01) -> None:
    """
    Display text with an animated effect.

    Args:
        text (str): The text to be displayed.
        delay (float, optional): The delay between each character.
        Default is 0.01 seconds.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
