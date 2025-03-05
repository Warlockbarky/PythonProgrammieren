"""Main module."""

import time
import minesweeper
from minesweeper import clear_console


def start_game():
    """
    Start a new game of Minesweeper.
    """
    # Choose game difficulty and number of mines
    difficulty, amount_of_mines = minesweeper.choose_difficulty()
    if difficulty is None:
        return

    clear_console()

    # Get the number of rows from the user
    while True:
        rows = minesweeper.animated_input("Enter the number of rows (5-99)"
                                          "(or 'quit' to exit to the menu): ")
        if rows.lower() == 'quit':
            return
        rows = int(rows)
        if 5 <= rows <= 99:
            break
        minesweeper.animated_text("Invalid number of rows. Please enter"
                                  "a number between 5 and 99.\n")

    # Get the number of columns from the user
    while True:
        cols = minesweeper.animated_input("Enter the number of columns (5-9)"
                                          "(or 'quit' to exit to the menu): ")
        if cols.lower() == 'quit':
            return
        cols = int(cols)
        if 5 <= cols <= 9:
            break
        minesweeper.animated_text("Invalid number of columns. Please"
                                  "enter a number between 5 and 9.\n")

    clear_console()

    # Generate the minesweeper board and print it
    board, rows, cols = minesweeper.generate_minesweeper_board(rows, cols)
    minesweeper.print_board(board)

    # Get the starting row and column from the user
    start_row = minesweeper.animated_input("Enter the starting row"
                                           "(or 'quit' to exit to the menu): ")
    if start_row.lower() == 'quit':
        return
    start_row = int(start_row)

    start_col = minesweeper.animated_input("Enter the starting column"
                                           "(or 'quit' to exit to the menu): ")
    if start_col.lower() == 'quit':
        return
    start_col = int(start_col)
    clear_console()

    # Start the game timer
    start_time = time.time()

    # Open cells and place mines on the board
    minesweeper.open_cells(board, rows, cols, start_row, start_col, difficulty)
    board_with_mines = minesweeper.place_mines(board, rows, cols, amount_of_mines)
    board_with_counts = minesweeper.count_adjacent_mines(board_with_mines, rows, cols)
    board_with_opened_neighbors = minesweeper.open_empty_neighbors(board_with_counts, rows, cols)
    board_with_hidden_mines = minesweeper.hide_mines(board_with_opened_neighbors, rows, cols)
    minesweeper.animated_text("Board with hidden mines:\n")
    minesweeper.print_board(board_with_hidden_mines)

    # Main game loop
    while True:
        row = minesweeper.animated_input("Enter the row"
                                         "(or 'quit' to exit to the menu): ")
        if row.lower() == 'quit':
            break
        row = int(row)

        col = minesweeper.animated_input("Enter the column"
                                         "(or 'quit' to exit to the menu): ")
        if col.lower() == 'quit':
            break
        col = int(col)
        clear_console()

        # Check if the user hit a mine
        if board_with_mines[row][col] == "*":
            minesweeper.animated_text("You lost!")
            minesweeper.animated_text("Board with mines:\n")
            minesweeper.print_board(board_with_opened_neighbors)
            choice = minesweeper.animated_input("To play again press 1\n"
                                                "To return to the main menu"
                                                "press 2\nYour choice: ")
            if choice == "1":
                start_game()
                return
            if choice == "2":
                break
            minesweeper.animated_text("Invalid choice."
                                      "Please try again.\n")

        # Open the selected cell
        if board_with_opened_neighbors[row][col] == "■":
            board_with_opened_neighbors[row][col] = " "

        # Update the board with counts and open empty neighbors
        board_with_counts = minesweeper.count_adjacent_mines(
            board_with_opened_neighbors, rows, cols
            )
        board_with_opened_neighbors = minesweeper.open_empty_neighbors(
            board_with_counts, rows, cols
            )

        # Check if the user has won
        if minesweeper.no_closed_cells(board_with_opened_neighbors, rows, cols):
            end_time = time.time()
            elapsed_time = end_time - start_time
            minesweeper.animated_text("You won! Game time: "
                                      f"{elapsed_time:.2f} seconds")
            minesweeper.animated_text("Board with mines:\n")
            minesweeper.print_board(board_with_opened_neighbors)
            choice = minesweeper.animated_input("To play again press 1\n"
                                                "To return to the main menu "
                                                "press 2\nYour choice: ")
            if choice == "1":
                start_game()
                return
            if choice == "2":
                break
            minesweeper.animated_text("Invalid choice. "
                                      "Please try again.\n")

        # Hide mines and print the board
        board_with_hidden_mines = minesweeper.hide_mines(board_with_opened_neighbors, rows, cols)
        minesweeper.animated_text("Board with hidden mines:\n")
        minesweeper.print_board(board_with_hidden_mines)


def main():
    """
    Main function to display the menu and start the game.
    """
    # Main menu loop
    while True:
        minesweeper.display_menu()
        choice = minesweeper.animated_input("Choose an action: ")

        if choice == "1":
            start_game()
        elif choice == "2":
            minesweeper.clear_console()
            minesweeper.animated_text("Exiting the game. Goodbye!")
            break
        else:
            minesweeper.animated_text("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
