"""Module to open the neighboring cells of empty cells on the board."""

import copy
from .count_adjacent_mines import count_adjacent_mines


def open_empty_neighbors(board: list[list[str]], rows: int, cols: int) -> list[list[str]]:
    """
    Args:
        board (list): The game board represented as a 2D list.
        rows (int): The number of rows in the board.
        cols (int): The number of columns in the board.

    Returns:
        list: The updated game board
        with neighboring cells of empty cells opened.
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def is_empty(r: int, c: int) -> bool:
        return board[r][c] == " "

    def open_neighbors(board_copy: list[list[str]], r: int, c: int) -> None:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= rows and 1 <= nc <= cols and board_copy[nr][nc] == "■":
                board_copy[nr][nc] = " "

    while True:
        board_copy = copy.deepcopy(board)
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if is_empty(r, c):
                    open_neighbors(board_copy, r, c)
        if board_copy == board:
            break
        board = count_adjacent_mines(board_copy, rows, cols)
    return board
