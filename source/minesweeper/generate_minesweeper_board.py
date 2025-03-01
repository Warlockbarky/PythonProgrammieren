def generate_minesweeper_board(rows: int, cols: int):
    # Determine the width needed for row numbers
    max_num_width = len(str(rows))
    # Create the initial board filled with "■" symbols
    board = [["■" for _ in range(cols)] for _ in range(rows)]

    # Create the header row with column numbers
    header = [" " * max_num_width] + [str(i) for i in range(1, cols + 1)]

    # Add row numbers to each row of the board
    board_with_labels = [[str(i).rjust(max_num_width)] + row for i, row in enumerate(board, start=1)]

    # Return the board with labels, and the number of rows and columns
    return [header] + board_with_labels, rows, cols
