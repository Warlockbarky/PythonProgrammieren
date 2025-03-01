def generate_minesweeper_board(rows: int, cols: int):
    max_num_width = len(str(rows))
    board = [["■" for _ in range(cols)] for _ in range(rows)]

    header = [" " * max_num_width] + [str(i) for i in range(1, cols + 1)]

    board_with_labels = [[str(i).rjust(max_num_width)] + row for i, row in enumerate(board, start=1)]

    return [header] + board_with_labels, rows, cols
