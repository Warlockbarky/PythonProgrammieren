"""Module to hide mines on a board."""

import copy


def hide_mines(board: list[list[str]], rows: int, cols: int) -> list[list[str]]:
    """
    Hide the mines on the board by replacing them with a placeholder.

    Args:
        board (list): The game board represented as a 2D list.
        rows (int): The number of rows in the board.
        cols (int): The number of columns in the board.

    Returns:
        list: A new board with the mines hidden.
    """
    board_with_hidden_mines = copy.deepcopy(board)
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if board_with_hidden_mines[r][c] == "*":
                board_with_hidden_mines[r][c] = "■"
    return board_with_hidden_mines
