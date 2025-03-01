import copy


def count_adjacent_mines(board, rows, cols):
    # Create a deep copy of the board to store mine counts
    board_with_counts = copy.deepcopy(board)
    # Define the 8 possible directions to check for adjacent mines
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    # Iterate over each cell in the board
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            # Check if the cell is empty
            if board[r][c] == " ":
                mine_count = 0
                # Check all adjacent cells for mines
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 1 <= nr <= rows and 1 <= nc <= cols and board_with_counts[nr][nc] == "*":
                        mine_count += 1
                # Update the cell with the count of adjacent mines or leave it empty
                board_with_counts[r][c] = str(mine_count) if mine_count > 0 else " "
    # Return the board with mine counts
    return board_with_counts
