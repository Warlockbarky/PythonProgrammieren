import time
import minesweeper
from minesweeper import current_user


def start_game():
    global current_user
    if current_user is None:
        username = minesweeper.manage_profiles()
        if not username:
            return
    else:
        username = current_user

    difficulty, amount_of_mines = minesweeper.choose_difficulty()
    if difficulty is None:
        return

    rows = input("Введите количество строк (или 'quit' для выхода в меню): ")
    if rows.lower() == 'quit':
        return
    rows = int(rows)

    cols = input("Введите количество столбцов (или 'quit' для выхода в меню): ")
    if cols.lower() == 'quit':
        return
    cols = int(cols)

    board, rows, cols = minesweeper.generate_minesweeper_board(rows, cols)
    minesweeper.print_board(board)

    start_row = input("Введите начальную строку (или 'quit' для выхода в меню): ")
    if start_row.lower() == 'quit':
        return
    start_row = int(start_row)

    start_col = input("Введите начальный столбец (или 'quit' для выхода в меню): ")
    if start_col.lower() == 'quit':
        return
    start_col = int(start_col)

    # Начало отсчета времени
    start_time = time.time()

    minesweeper.open_cells(board, rows, cols, start_row, start_col, difficulty)
    board_with_mines = minesweeper.place_mines(board, rows, cols, amount_of_mines)
    board_with_counts = minesweeper.count_adjacent_mines(board_with_mines, rows, cols)
    board_with_opened_neighbors = minesweeper.open_empty_neighbors(board_with_counts, rows, cols)
    board_with_hidden_mines = minesweeper.hide_mines(board_with_opened_neighbors, rows, cols)
    print("Поле с скрытыми минами:")
    minesweeper.print_board(board_with_hidden_mines)

    while True:
        row = input("Введите строку (или 'quit' для выхода в меню): ")
        if row.lower() == 'quit':
            break
        row = int(row)

        col = input("Введите столбец (или 'quit' для выхода в меню): ")
        if col.lower() == 'quit':
            break
        col = int(col)

        if board_with_mines[row][col] == "*":
            print("Вы проиграли!")
            print("Поле с минами:")
            minesweeper.print_board(board_with_opened_neighbors)
            break

        if board_with_opened_neighbors[row][col] == "■":
            board_with_opened_neighbors[row][col] = " "

        board_with_counts = minesweeper.count_adjacent_mines(board_with_opened_neighbors, rows, cols)
        board_with_opened_neighbors = minesweeper.open_empty_neighbors(board_with_counts, rows, cols)

        if minesweeper.no_closed_cells(board_with_opened_neighbors, rows, cols):
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Вы выиграли! Время игры: {elapsed_time:.2f} секунд")
            print("Поле с минами:")
            minesweeper.print_board(board_with_opened_neighbors)
            update_records(username, rows, cols, difficulty, elapsed_time)
            break

        board_with_hidden_mines = minesweeper.hide_mines(board_with_opened_neighbors, rows, cols)
        print("Поле с скрытыми минами:")
        minesweeper.print_board(board_with_hidden_mines)


def main():
    while True:
        minesweeper.display_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            start_game()
        elif choice == "2":
            minesweeper.profile_management()
        elif choice == "3":
            minesweeper.display_records()
        elif choice == "4":
            print("Выход из игры. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
