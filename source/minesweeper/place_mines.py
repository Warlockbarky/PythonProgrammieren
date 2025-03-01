import random
import copy


def place_mines(board, rows, cols, difficulty: int):
    # Create a deep copy of the board to place mines
    board_with_mines = copy.deepcopy(board)
    # Calculate the total number of cells on the board
    total_cells = rows * cols
    # Determine the maximum number of mines based on difficulty
    max_mines = total_cells // difficulty
    # Get a list of all closed cells
    closed_cells = [(r, c) for r in range(1, rows + 1) for c in range(1, cols + 1) if board_with_mines[r][c] == "■"]
    # Randomly select positions for the mines
    mine_positions = random.sample(closed_cells, min(len(closed_cells), max_mines))
    # Place mines at the selected positions
    for r, c in mine_positions:
        board_with_mines[r][c] = "*"
    # Return the board with mines placed
    return board_with_mines
