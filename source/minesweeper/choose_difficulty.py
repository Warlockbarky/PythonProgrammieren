from .animated_input import animated_input
from .animated_text import animated_text
from .clear_console import clear_console


def choose_difficulty():
    clear_console()
    animated_text("Выберите уровень сложности:")
    animated_text("1. Легкий")
    animated_text("2. Средний")
    animated_text("3. Тяжелый")
    animated_text("4. Невозможный")

    while True:
        choice = animated_input("Введите номер уровня сложности (или 'quit' для выхода в меню): ")
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
            animated_text("Неверный выбор. Попробуйте снова.")
