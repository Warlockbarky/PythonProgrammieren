"""Module to check if there are no closed cells on the board."""


def no_closed_cells(board: list[list[str]], rows: int, cols: int) -> bool:
    """
    Args:
        board (list): The game board represented as a 2D list.
        rows (int): The number of rows in the board.
        cols (int): The number of columns in the board.

    Returns:
        bool: True if there are no closed cells, False otherwise.
    """
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if board[r][c] == "■":
                return False
    return True
