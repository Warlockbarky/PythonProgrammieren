from .animated_text import animated_text


def animated_input(prompt, delay=0.01):
    animated_text(prompt, delay)
    return input()
