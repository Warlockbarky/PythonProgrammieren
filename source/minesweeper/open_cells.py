import random


def open_cells(board, rows, cols, start_row: int, start_col: int, difficulty: int):
    # Calculate the total number of cells on the board
    total_cells = rows * cols
    # Determine the target number of cells to open based on difficulty
    target_open_cells = total_cells * difficulty // 100
    # Initialize a set to keep track of opened cells
    opened = set()
    # Initialize a queue with the starting cell
    queue = [(start_row, start_col)]

    while queue and len(opened) < target_open_cells:
        # Get the next cell from the queue
        r, c = queue.pop(0)
        # Skip if the cell is already opened or is on the border
        if (r, c) in opened or r == 0 or c == 0:
            continue
        # Open the cell
        board[r][c] = " "
        # Add the cell to the set of opened cells
        opened.add((r, c))
        # Get the neighboring cells
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        # Shuffle the neighbors to randomize the opening process
        random.shuffle(neighbors)
        # Add valid neighbors to the queue
        for nr, nc in neighbors:
            if 0 < nr <= rows and 0 < nc <= cols and (nr, nc) not in opened:
                queue.append((nr, nc))
