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
    while True:
        rows = minesweeper.animated_input("Enter the number of rows (5-99) (or 'quit' to exit to the menu): ")
        if rows.lower() == 'quit':
            return
        rows = int(rows)
        if 5 <= rows <= 99:
            break
        else:
            minesweeper.animated_text("Invalid number of rows. Please enter a number between 5 and 99.\n")

    while True:
        cols = minesweeper.animated_input("Enter the number of columns (5-9) (or 'quit' to exit to the menu): ")
        if cols.lower() == 'quit':
            return
        cols = int(cols)
        if 5 <= cols <= 9:
            break
        else:
            minesweeper.animated_text("Invalid number of columns. Please enter a number between 5 and 9.\n")

    clear_console()
    board, rows, cols = minesweeper.generate_minesweeper_board(rows, cols)
    minesweeper.print_board(board)

    start_row = minesweeper.animated_input("Enter the starting row (or 'quit' to exit to the menu): ")
    if start_row.lower() == 'quit':
        return
    start_row = int(start_row)

    start_col = minesweeper.animated_input("Enter the starting column (or 'quit' to exit to the menu): ")
    if start_col.lower() == 'quit':
        return
    start_col = int(start_col)
    clear_console()
    # Start the timer
    start_time = time.time()

    minesweeper.open_cells(board, rows, cols, start_row, start_col, difficulty)
    board_with_mines = minesweeper.place_mines(board, rows, cols, amount_of_mines)
    board_with_counts = minesweeper.count_adjacent_mines(board_with_mines, rows, cols)
    board_with_opened_neighbors = minesweeper.open_empty_neighbors(board_with_counts, rows, cols)
    board_with_hidden_mines = minesweeper.hide_mines(board_with_opened_neighbors, rows, cols)
    minesweeper.animated_text("Board with hidden mines:\n")
    minesweeper.print_board(board_with_hidden_mines)

    while True:
        row = minesweeper.animated_input("Enter the row (or 'quit' to exit to the menu): ")
        if row.lower() == 'quit':
            break
        row = int(row)

        col = minesweeper.animated_input("Enter the column (or 'quit' to exit to the menu): ")
        if col.lower() == 'quit':
            break
        col = int(col)
        clear_console()

        if board_with_mines[row][col] == "*":
            minesweeper.animated_text("You lost!")
            minesweeper.animated_text("Board with mines:\n")
            minesweeper.print_board(board_with_opened_neighbors)
            choice = minesweeper.animated_input("To play again press 1\nTo return to the main menu press 2\nYour choice: ")
            if choice == "1":
                start_game()
                return
            elif choice == "2":
                break
            else:
                minesweeper.animated_text("Invalid choice. Please try again.\n")

        if board_with_opened_neighbors[row][col] == "■":
            board_with_opened_neighbors[row][col] = " "

        board_with_counts = minesweeper.count_adjacent_mines(board_with_opened_neighbors, rows, cols)
        board_with_opened_neighbors = minesweeper.open_empty_neighbors(board_with_counts, rows, cols)

        if minesweeper.no_closed_cells(board_with_opened_neighbors, rows, cols):
            end_time = time.time()
            elapsed_time = end_time - start_time
            minesweeper.animated_text(f"You won! Game time: {elapsed_time:.2f} seconds")
            minesweeper.animated_text("Board with mines:\n")
            minesweeper.print_board(board_with_opened_neighbors)
            minesweeper.update_records(username, rows, cols, difficulty, elapsed_time)
            choice = minesweeper.animated_input("To play again press 1\nTo return to the main menu press 2\nYour choice: ")
            if choice == "1":
                start_game()
                return
            elif choice == "2":
                break
            else:
                minesweeper.animated_text("Invalid choice. Please try again.\n")

        board_with_hidden_mines = minesweeper.hide_mines(board_with_opened_neighbors, rows, cols)
        minesweeper.animated_text("Board with hidden mines:\n")
        minesweeper.print_board(board_with_hidden_mines)


def main():
    while True:
        minesweeper.display_menu()
        choice = minesweeper.animated_input("Choose an action: ")

        if choice == "1":
            start_game()
        elif choice == "2":
            minesweeper.profile_management()
        elif choice == "3":
            minesweeper.display_records()
        elif choice == "4":
            minesweeper.clear_console()
            minesweeper.animated_text("Exiting the game. Goodbye!")
            break
        else:
            minesweeper.animated_text("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
