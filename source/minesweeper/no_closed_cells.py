def no_closed_cells(board, rows, cols):
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if board[r][c] == "■":
                return False
    return True
