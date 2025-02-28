import copy


def count_adjacent_mines(board, rows, cols):
    board_with_counts = copy.deepcopy(board)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if board[r][c] == " ":
                mine_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 1 <= nr <= rows and 1 <= nc <= cols and board_with_counts[nr][nc] == "*":
                        mine_count += 1
                board_with_counts[r][c] = str(mine_count) if mine_count > 0 else " "
    return board_with_counts
