import json
import os
import getpass
from .animated_input import animated_input
from .animated_text import animated_text
from .clear_console import clear_console

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
    username = animated_input("Enter username: ")
    if username.lower() == 'quit':
        return None
    if username in profiles:
        animated_text("A profile with this username already exists.")
        return None

    password = getpass.getpass("Enter password: ")
    if password.lower() == 'quit':
        return None
    profiles[username] = password
    save_profiles(profiles)
    animated_text("Profile successfully created.")
    return username


def login_profile(profiles):
    clear_console()
    username = animated_input("Enter username: ")
    if username.lower() == 'quit':
        return None
    if username not in profiles:
        animated_text("Profile with this username not found.")
        return None

    password = getpass.getpass("Enter password: ")
    if password.lower() == 'quit':
        return None
    if profiles[username] != password:
        animated_text("Incorrect password.")
        return None

    animated_text("Successfully logged in.")
    return username


def manage_profiles():
    clear_console()
    global current_user
    profiles = load_profiles()
    while True:
        choice = animated_input("1. Log in\n2. Create profile\n3. Return to menu\nChoose an action: ")
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
            animated_text("Invalid choice. Please try again.")


def profile_management():
    global current_user
    if current_user is None:
        animated_text("You are not logged in.")
        username = manage_profiles()
        if not username:
            return

    profiles = load_profiles()
    while True:
        clear_console()
        choice = animated_input("1. Change username\n2. Change password\n3. Log out\n4. Return to menu\nChoose an action: ")
        if choice == "1":
            new_username = animated_input("Enter new username: ")
            if new_username in profiles:
                animated_text("A profile with this username already exists.")
            else:
                profiles[new_username] = profiles.pop(current_user)
                save_profiles(profiles)
                current_user = new_username
                animated_text("Username successfully changed.")
        elif choice == "2":
            new_password = getpass.getpass("Enter new password: ")
            profiles[current_user] = new_password
            save_profiles(profiles)
            animated_text("Password successfully changed.")
        elif choice == "3":
            current_user = None
            animated_text("Logged out.")
            break
        elif choice == "4":
            break
        else:
            animated_text("Invalid choice. Please try again.")


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
    key = f"{rows}x{cols} {difficulty_text}"
    if key not in user_records["best_times"] or elapsed_time < user_records["best_times"][key]:
        user_records["best_times"][key] = elapsed_time

    records[username] = user_records
    save_records(records)


def display_records():
    global current_user
    if current_user is None:
        animated_text("You are not logged in.")
        choice = animated_input("Press 1 to return to the main menu\nYour choice: ")
    while choice != "1":
        animated_text("Invalid choice. Please try again.")
        choice = animated_input("Press 1 to return to the main menu\nYour choice: ")
    if choice == "1":
        return

    records = load_records()
    user_records = records.get(current_user, {"wins": 0, "best_times": {}})
    animated_text(f"Best records for {current_user}:")
    for key, time in user_records["best_times"].items():
        animated_text(f"{key}: {time:.2f} seconds")
    animated_text(f"Total wins: {user_records['wins']}\n")
    choice = animated_input("Press 1 to return to the main menu\nYour choice: ")
    while choice != "1":
        animated_text("Invalid choice. Please try again.")
        choice = animated_input("Press 1 to return to the main menu\nYour choice: ")
    if choice == "1":
        return
