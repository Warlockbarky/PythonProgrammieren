"""Module to print the Minesweeper board with colored cells."""

from colorama import Fore, Style


def print_board(board: list[list[str]]) -> None:
    """
    Args:
        board (list): The game board represented as a 2D list.
    """
    # Define a color map for different cell values
    color_map = {
        '1': Fore.BLUE,
        '2': Fore.GREEN,
        '3': Fore.RED,
        '4': Fore.CYAN,
        '5': Fore.MAGENTA,
        '6': Fore.YELLOW,
        '7': Fore.WHITE,
        '8': Fore.LIGHTBLACK_EX
    }

    for i, row in enumerate(board):
        colored_row = []
        for j, cell in enumerate(row):
            # Apply color to the cell if it is in the color map
            # and not in the header row/column
            if i > 0 and j > 0 and cell in color_map:
                colored_row.append(color_map[cell] + cell + Style.RESET_ALL)
            else:
                colored_row.append(cell)
        # Print the row with colored cells
        print(" ".join(colored_row))
