T = int(input()) # 10개의 case를 받을것.

for case in range(1, T+1): # 형식맞추기
    max_sum = 0            # max_sum은 case 할때마다 refresh
    matrix_size, screen = map(int, input().split()) # size x size의 행렬, screen x screen의 파리채
    given_matrix = [list(map(int, input().split())) for _ in range(matrix_size)]

    max_start_coordinate = matrix_size - screen + 1
    # 기준점이 row, col 각각 0 ~ (matrix_size- screen) -1. 이래야 matrix_size + (screen-1)
    # 7 5 들어갔을때, 2 ->여기서 잘못. 되서. 0 1 2 3 4 5 6 중에, 0 1 2 앵커로 받고, 2 3 4 5 6 d_row/col으로 받음.
    for anchor_row in range(max_start_coordinate):
        for anchor_col in range(max_start_coordinate):
            temp_sum = 0
            for d_row in range(screen):
                for d_col in range(screen):
                    temp_sum += given_matrix[anchor_row+d_row][anchor_col+d_col]

            if temp_sum > max_sum:
                max_sum = temp_sum
    print(f'#{case} {max_sum}')