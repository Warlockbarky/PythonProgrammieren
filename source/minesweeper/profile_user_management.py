import json
import os
import getpass

PROFILES_FILE = 'profiles.json'
RECORDS_FILE = 'records.json'
current_user = None


def load_profiles():
    if not os.path.exists(PROFILES_FILE):
        return {}
    with open(PROFILES_FILE, 'r') as file:
        return json.load(file)


def save_profiles(profiles):
    with open(PROFILES_FILE, 'w') as file:
        json.dump(profiles, file)


def load_records():
    if not os.path.exists(RECORDS_FILE):
        return {}
    with open(RECORDS_FILE, 'r') as file:
        return json.load(file)


def save_records(records):
    with open(RECORDS_FILE, 'w') as file:
        json.dump(records, file)


def register_profile(profiles):
    username = input("Введите ник: ")
    if username.lower() == 'quit':
        return None
    if username in profiles:
        print("Профиль с таким ником уже существует.")
        return None

    password = getpass.getpass("Введите пароль: ")
    if password.lower() == 'quit':
        return None
    profiles[username] = password
    save_profiles(profiles)
    print("Профиль успешно создан.")
    return username


def login_profile(profiles):
    username = input("Введите ник: ")
    if username.lower() == 'quit':
        return None
    if username not in profiles:
        print("Профиль с таким ником не найден.")
        return None

    password = getpass.getpass("Введите пароль: ")
    if password.lower() == 'quit':
        return None
    if profiles[username] != password:
        print("Неверный пароль.")
        return None

    print("Вы успешно вошли в профиль.")
    return username


def manage_profiles():
    global current_user
    profiles = load_profiles()
    while True:
        choice = input("1. Войти в профиль\n2. Создать профиль\n3. Вернуться в меню\nВыберите действие: ")
        if choice == "1":
            username = login_profile(profiles)
            if username:
                current_user = username
                return username
        elif choice == "2":
            username = register_profile(profiles)
            if username:
                current_user = username
                return username
        elif choice == "3":
            return None
        else:
            print("Неверный выбор. Попробуйте снова.")


def profile_management():
    global current_user
    if current_user is None:
        print("Вы не вошли в профиль.")
        username = manage_profiles()
        if not username:
            return

    profiles = load_profiles()
    while True:
        choice = input("1. Изменить ник\n2. Изменить пароль\n3. Выйти из профиля\n4. Вернуться в меню\nВыберите действие: ")
        if choice == "1":
            new_username = input("Введите новый ник: ")
            if new_username in profiles:
                print("Профиль с таким ником уже существует.")
            else:
                profiles[new_username] = profiles.pop(current_user)
                save_profiles(profiles)
                current_user = new_username
                print("Ник успешно изменен.")
        elif choice == "2":
            new_password = getpass.getpass("Введите новый пароль: ")
            profiles[current_user] = new_password
            save_profiles(profiles)
            print("Пароль успешно изменен.")
        elif choice == "3":
            current_user = None
            print("Вы вышли из профиля.")
            break
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def difficulty_to_text(difficulty):
    if difficulty == 30:
        return "easy"
    elif difficulty == 25:
        return "medium"
    elif difficulty == 20:
        return "hard"
    elif difficulty == 10:
        return "impossible"
    else:
        return "unknown"


def update_records(username, rows, cols, difficulty, elapsed_time):
    records = load_records()
    user_records = records.get(username, {"wins": 0, "best_times": {}})
    user_records["wins"] += 1

    difficulty_text = difficulty_to_text(difficulty)
    key = f"{rows}x{cols}_{difficulty_text}"
    if key not in user_records["best_times"] or elapsed_time < user_records["best_times"][key]:
        user_records["best_times"][key] = elapsed_time

    records[username] = user_records
    save_records(records)


def display_records():
    global current_user
    if current_user is None:
        print("Вы не вошли в профиль.")
        return

    records = load_records()
    user_records = records.get(current_user, {"wins": 0, "best_times": {}})
    print(f"Лучшие результаты для {current_user}:")
    for key, time in user_records["best_times"].items():
        print(f"{key}: {time:.2f} секунд")
    print(f"Общее количество выигрышей: {user_records['wins']}")