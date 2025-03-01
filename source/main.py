import time
import minesweeper
from minesweeper import profile_user_management
from minesweeper import clear_console


def start_game():
    if profile_user_management.current_user is None:
        username = minesweeper.manage_profiles()
        if not username:
            return
    else:
        username = profile_user_management.current_user

    difficulty, amount_of_mines = minesweeper.choose_difficulty()
    if difficulty is None:
        return

    clear_console()
    rows = minesweeper.animated_input("Введите количество строк (или 'quit' для выхода в меню): ")
    if rows.lower() == 'quit':
        return
    rows = int(rows)

    cols = minesweeper.animated_input("Введите количество столбцов (или 'quit' для выхода в меню): ")
    if cols.lower() == 'quit':
        return
    cols = int(cols)

    clear_console()
    board, rows, cols = minesweeper.generate_minesweeper_board(rows, cols)
    minesweeper.print_board(board)

    start_row = minesweeper.animated_input("Введите начальную строку (или 'quit' для выхода в меню): ")
    if start_row.lower() == 'quit':
        return
    start_row = int(start_row)

    start_col = minesweeper.animated_input("Введите начальный столбец (или 'quit' для выхода в меню): ")
    if start_col.lower() == 'quit':
        return
    start_col = int(start_col)
    clear_console()
    # Начало отсчета времени
    start_time = time.time()

    minesweeper.open_cells(board, rows, cols, start_row, start_col, difficulty)
    board_with_mines = minesweeper.place_mines(board, rows, cols, amount_of_mines)
    board_with_counts = minesweeper.count_adjacent_mines(board_with_mines, rows, cols)
    board_with_opened_neighbors = minesweeper.open_empty_neighbors(board_with_counts, rows, cols)
    board_with_hidden_mines = minesweeper.hide_mines(board_with_opened_neighbors, rows, cols)
    minesweeper.animated_text("Поле с скрытыми минами:\n")
    minesweeper.print_board(board_with_hidden_mines)

    while True:
        row = minesweeper.animated_input("Введите строку (или 'quit' для выхода в меню): ")
        if row.lower() == 'quit':
            break
        row = int(row)

        col = minesweeper.animated_input("Введите столбец (или 'quit' для выхода в меню): ")
        if col.lower() == 'quit':
            break
        col = int(col)
        clear_console()

        if board_with_mines[row][col] == "*":
            minesweeper.animated_text("Вы проиграли!")
            minesweeper.animated_text("Поле с минами:\n")
            minesweeper.print_board(board_with_opened_neighbors)
            choice = minesweeper.animated_input("Чтобы сыграть заново нажмите 1\nЧтобы вернутся в главное меню нажмите 2\nВаш выбор: ")
            if choice == "1":
                start_game()
                return
            elif choice == "2":
                break
            else:
                minesweeper.animated_text("Неверный выбор. Попробуйте снова.\n")

        if board_with_opened_neighbors[row][col] == "■":
            board_with_opened_neighbors[row][col] = " "

        board_with_counts = minesweeper.count_adjacent_mines(board_with_opened_neighbors, rows, cols)
        board_with_opened_neighbors = minesweeper.open_empty_neighbors(board_with_counts, rows, cols)

        if minesweeper.no_closed_cells(board_with_opened_neighbors, rows, cols):
            end_time = time.time()
            elapsed_time = end_time - start_time
            minesweeper.animated_text(f"Вы выиграли! Время игры: {elapsed_time:.2f} секунд")
            minesweeper.animated_text("Поле с минами:\n")
            minesweeper.print_board(board_with_opened_neighbors)
            minesweeper.update_records(username, rows, cols, difficulty, elapsed_time)
            choice = minesweeper.animated_input("Чтобы сыграть заново нажмите 1\nЧтобы вернутся в главное меню нажмите 2\nВаш выбор: ")
            if choice == "1":
                start_game()
                return
            elif choice == "2":
                break
            else:
                minesweeper.animated_text("Неверный выбор. Попробуйте снова.\n")

        board_with_hidden_mines = minesweeper.hide_mines(board_with_opened_neighbors, rows, cols)
        minesweeper.animated_text("Поле с скрытыми минами:\n")
        minesweeper.print_board(board_with_hidden_mines)


def main():
    while True:
        minesweeper.display_menu()
        choice = minesweeper.animated_input("Выберите действие: ")

        if choice == "1":
            start_game()
        elif choice == "2":
            minesweeper.profile_management()
        elif choice == "3":
            minesweeper.display_records()
        elif choice == "4":
            minesweeper.clear_console()
            minesweeper.animated_text("Выход из игры. До свидания!")
            break
        else:
            minesweeper.animated_text("Неверный выбор. Попробуйте снова.\n")


if __name__ == "__main__":
    main()
