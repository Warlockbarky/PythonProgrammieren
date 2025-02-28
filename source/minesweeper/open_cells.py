import random


def open_cells(board, rows, cols, start_row: int, start_col: int, difficulty: int):
    total_cells = rows * cols
    target_open_cells = total_cells * difficulty // 100
    opened = set()
    queue = [(start_row, start_col)]

    while queue and len(opened) < target_open_cells:
        r, c = queue.pop(0)
        if (r, c) in opened or r == 0 or c == 0:
            continue
        board[r][c] = " "
        opened.add((r, c))
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        random.shuffle(neighbors)
        for nr, nc in neighbors:
            if 0 < nr <= rows and 0 < nc <= cols and (nr, nc) not in opened:
                queue.append((nr, nc))
