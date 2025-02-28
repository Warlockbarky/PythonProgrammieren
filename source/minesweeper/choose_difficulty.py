def choose_difficulty():
    print("Выберите уровень сложности:")
    print("1. Легкий")
    print("2. Средний")
    print("3. Тяжелый")
    print("4. Невозможный")

    while True:
        choice = input("Введите номер уровня сложности (или 'quit' для выхода в меню): ")
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
            print("Неверный выбор. Попробуйте снова.")
