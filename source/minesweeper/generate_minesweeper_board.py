def generate_minesweeper_board(rows: int, cols: int):
    board = [["■" for _ in range(cols)] for _ in range(rows)]
    board_with_labels = [[str(i)] + row for i, row in enumerate(board, start=1)]
    header = [" "] + [str(i) for i in range(1, cols + 1)]
    return [header] + board_with_labels, rows, cols
