from .clear_console import clear_console
from .animated_text import animated_text


def display_menu():
    clear_console()
    animated_text("Добро пожаловать в игру Сапер!")
    animated_text("1. Начать игру")
    animated_text("2. Управление профилем")
    animated_text("3. Посмотреть рекорды")
    animated_text("4. Выйти")
