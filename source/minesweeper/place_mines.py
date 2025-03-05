"""Module to place mines on the board based on the difficulty level."""


import random
import copy


def place_mines(board, rows, cols, difficulty: int):
    """
    Args:
        board (list): The game board represented as a 2D list.
        rows (int): The number of rows in the board.
        cols (int): The number of columns in the board.
        difficulty (int): The difficulty level determining the number of mines.

    Returns:
        list: The board with mines placed.
    """
    board_with_mines = copy.deepcopy(board)
    total_cells = rows * cols
    max_mines = total_cells // difficulty
    closed_cells = [(r, c) for r in range(1, rows + 1) for c in
                    range(1, cols + 1) if board_with_mines[r][c] == "■"]
    mine_positions = random.sample(closed_cells, min(len(closed_cells), max_mines))
    for r, c in mine_positions:
        board_with_mines[r][c] = "*"
    return board_with_mines
