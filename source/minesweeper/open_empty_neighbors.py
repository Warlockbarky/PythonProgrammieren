import copy
from . import count_adjacent_mines


def open_empty_neighbors(board, rows, cols):
    # Define the 8 possible directions to check for neighbors
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Check if a cell is empty
    def is_empty(r, c):
        return board[r][c] == " "

    # Open the neighboring cells of an empty cell
    def open_neighbors(board_copy, r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= rows and 1 <= nc <= cols and board_copy[nr][nc] == "■":
                board_copy[nr][nc] = " "

    while True:
        # Create a deep copy of the board to track changes
        board_copy = copy.deepcopy(board)
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if is_empty(r, c):
                    open_neighbors(board_copy, r, c)
        # Break the loop if no changes were made
        if board_copy == board:
            break
        # Update the board with the new state
        board = count_adjacent_mines(board_copy, rows, cols)
    return board
