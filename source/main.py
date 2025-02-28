import random
import copy

def generate_minesweeper_board(rows: int, cols: int):
    """
    Генерирует пустое игровое поле для Сапёра заданного размера с номерами строк и столбцов (начиная с 1).
    :param rows: Количество строк
    :param cols: Количество столбцов
    :return: Двумерный список (игровое поле)
    """
    board = [["■" for _ in range(cols)] for _ in range(rows)]
    
    # Добавление номеров строк (нумерация с 1)
    board_with_labels = [[str(i)] + row for i, row in enumerate(board, start=1)]
    
    # Создание заголовков столбцов (нумерация с 1)
    header = [" "] + [str(i) for i in range(1, cols + 1)]
    
    return [header] + board_with_labels, rows, cols

def open_cells(board, rows, cols, start_row: int, start_col: int):
    """
    Открывает клетку и распространяет открытие на соседние клетки, пока не достигнем 30% открытых клеток.
    :param board: Игровое поле
    :param rows: Количество строк
    :param cols: Количество столбцов
    :param start_row: Начальная строка (1-индексация)
    :param start_col: Начальный столбец (1-индексация)
    """
    total_cells = rows * cols
    target_open_cells = total_cells * 30 // 100  # 30% от всех клеток, округляя вниз
    opened = set()
    queue = [(start_row, start_col)]  # Остается в 1-индексации
    
    while queue and len(opened) < target_open_cells:
        r, c = queue.pop(0)  # Используем pop(0) для извлечения первого элемента
        if (r, c) in opened or r == 0 or c == 0:  # Пропускаем заголовки
            continue
        
        board[r][c] = " "  # Открытая клетка
        opened.add((r, c))
        
        # Проверяем соседей (вверх, вниз, влево, вправо)
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        random.shuffle(neighbors)  # Перемешиваем для равномерного распределения
        
        for nr, nc in neighbors:
            if 0 < nr <= rows and 0 < nc <= cols and (nr, nc) not in opened:
                queue.append((nr, nc))

def place_mines(board, rows, cols):
    """
    Создает копию доски и расставляет мины на закрытых клетках (■), не превышая 1/6 от общего числа клеток.
    :param board: Игровое поле
    :param rows: Количество строк
    :param cols: Количество столбцов
    :return: Копия доски с минами
    """
    board_with_mines = copy.deepcopy(board)
    total_cells = rows * cols
    max_mines = total_cells // 6  # 1/6 от всех клеток
    closed_cells = [(r, c) for r in range(1, rows + 1) for c in range(1, cols + 1) if board_with_mines[r][c] == "■"]
    
    mine_positions = random.sample(closed_cells, min(len(closed_cells), max_mines))
    
    for r, c in mine_positions:
        board_with_mines[r][c] = "*"  # Обозначение мины
    
    return board_with_mines

def count_adjacent_mines(board, rows, cols):
    """
    Создает копию доски и обновляет её, заполняя каждую изначально открытую клетку количеством мин, граничащих с ней.
    :param board: Игровое поле с минами
    :param rows: Количество строк
    :param cols: Количество столбцов
    :return: Копия обновленной доски
    """
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

def open_empty_neighbors(board, rows, cols):
    """
    Создает копию поля с подсчитанными минами и открывает все закрытые соседние поля для пустых клеток на оригинальном поле.
    :param board: Игровое поле с подсчитанными минами
    :param rows: Количество строк
    :param cols: Количество столбцов
    :return: Копия обновленной доски
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    def is_empty(r, c):
        return board[r][c] == " "
    
    def open_neighbors(board_copy, r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= rows and 1 <= nc <= cols and board_copy[nr][nc] == "■":
                board_copy[nr][nc] = " "  # Открываем закрытую клетку
    
    while True:
        board_copy = copy.deepcopy(board)
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if is_empty(r, c):
                    open_neighbors(board_copy, r, c)
        
        if board_copy == board:
            break
        
        board = count_adjacent_mines(board_copy, rows, cols)
    
    return board

def no_closed_cells(board, rows, cols):
    """
    Проверяет, есть ли на поле хотя бы одна закрытая клетка.
    :param board: Игровое поле
    :param rows: Количество строк
    :param cols: Количество столбцов
    :return: True, если нет ни одной закрытой клетки, иначе False
    """
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if board[r][c] == "■":
                return False
    return True

def hide_mines(board, rows, cols):
    """
    Заменяет мины на закрытые клетки в полученной таблице.
    :param board: Игровое поле с подсчитанными минами
    :param rows: Количество строк
    :param cols: Количество столбцов
    :return: Обновленная доска
    """
    board_with_hidden_mines = copy.deepcopy(board)
    
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if board_with_hidden_mines[r][c] == "*":
                board_with_hidden_mines[r][c] = "■"  # Заменяем мину на закрытую клетку
    
    return board_with_hidden_mines

# Тестирование функции
def print_board(board):
    for row in board:
        print(" ".join(row))

# Пример работы
board, rows, cols = generate_minesweeper_board(10, 10)
print_board(board)
open_cells(board, rows, cols, 3, 3)  # Открытие клетки (3,3) и распространение
print("Исходное поле:")
print_board(board)
board_with_mines = place_mines(board, rows, cols)  # Создание копии доски с минами
print("Поле с минами:")
print_board(board_with_mines)
board_with_counts = count_adjacent_mines(board_with_mines, rows, cols)
print("Поле с подсчетом мин:")
print_board(board_with_counts)
board_with_opened_neighbors = open_empty_neighbors(board_with_counts, rows, cols)  # Открытие соседних клеток
print("Поле с открытыми соседними клетками:")
print_board(board_with_opened_neighbors)
board_with_counts = count_adjacent_mines(board_with_opened_neighbors, rows, cols)
print("Поле с подсчетом мин:")
print_board(board_with_counts)
if no_closed_cells(board_with_counts, rows, cols):
    print("На поле нет закрытых клеток.")
else:
    print("На поле есть закрытые клетки.")
board_with_hidden_mines = hide_mines(count_adjacent_mines(board_with_opened_neighbors, rows, cols), rows, cols)  # Скрытие мин
print("Поле с скрытыми минами:")
print_board(board_with_hidden_mines)
