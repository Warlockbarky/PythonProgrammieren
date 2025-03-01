import sys
import time


def animated_text(text, delay=0.01):
    # Iterate over each character in the text
    for char in text:
        # Write the character to the standard output
        sys.stdout.write(char)
        # Flush the output buffer to ensure the character is displayed immediately
        sys.stdout.flush()
        # Pause for a short duration to create the animation effect
        time.sleep(delay)
    # Print a newline character after the animation is complete
    print()
