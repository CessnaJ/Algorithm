T = int(input())

def stamp_sum(ro, co):
    stamp_sum = 0
    for i in range(stamp_size):
        for j in range(stamp_size):
            stamp_sum += matrix[row+i][col+j]
    return stamp_sum


for case in range(1, T+1):
    stamp_sum_list = []
    matrix_size, stamp_size = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(matrix_size)]

    for row in range(matrix_size - stamp_size + 1):
        for col in range(matrix_size - stamp_size + 1):
            stamp_sum_list.append(stamp_sum(row, col))

    print(f'#{case} {max(stamp_sum_list)}')