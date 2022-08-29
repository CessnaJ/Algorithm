T = int(input())
unit_verification = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def small_box_unit(start_row,start_col):
    unit = []
    for row in range(start_row, start_row+3):
        for col in range(start_col, start_col+3):
            unit.append(sudoku_matrix[row][col])
    return sorted(unit)


for case in range(1, T+1):
    matching = 1
    sudoku_matrix = [list(map(int, input().split())) for _ in range(9)]

    for row in range(9):
        parallel_row = []
        crossing_col = []
        for col in range(9):
            parallel_row.append(sudoku_matrix[row][col])
            crossing_col.append(sudoku_matrix[col][row])
        if sorted(parallel_row) != unit_verification:
            matching = 0
        if sorted(crossing_col) != unit_verification:
            matching = 0

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            # print(row, col)
            if small_box_unit(row, col) != unit_verification:
                matching = 0

    print(f'#{case} {matching}')