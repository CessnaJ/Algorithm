T = int(input())


for case in range(1, T+1):
    matrix_size = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(matrix_size)]
    diamond_sum = 0
    for row in range(matrix_size):
        if 0 <= row <= matrix_size//2:
            diamond_sum += sum(matrix[row][abs(matrix_size//2 - row): matrix_size//2 + row + 1])
        else:
            diamond_sum += sum(matrix[row][abs(matrix_size//2 - row): (3 * (matrix_size//2)) - row + 1])


    print(f'#{case} {diamond_sum}')