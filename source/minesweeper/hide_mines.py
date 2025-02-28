import copy


def hide_mines(board, rows, cols):
    board_with_hidden_mines = copy.deepcopy(board)
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if board_with_hidden_mines[r][c] == "*":
                board_with_hidden_mines[r][c] = "■"
    return board_with_hidden_mines
