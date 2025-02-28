import random
import copy


def place_mines(board, rows, cols, difficulty: int):
    board_with_mines = copy.deepcopy(board)
    total_cells = rows * cols
    max_mines = total_cells // difficulty
    closed_cells = [(r, c) for r in range(1, rows + 1) for c in range(1, cols + 1) if board_with_mines[r][c] == "■"]
    mine_positions = random.sample(closed_cells, min(len(closed_cells), max_mines))
    for r, c in mine_positions:
        board_with_mines[r][c] = "*"
    return board_with_mines
