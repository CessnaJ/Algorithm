rows, columns = map(int, input().split())
# 200 * 200 -> 40000개의 칸.
matrix = [list(map(int, input().split())) for _ in range(rows)]

# 행의 합이 끝날때마다 검사를 통해 마이너스가 되면 그 시행을 prunning 해주면 되지 않을까 - 어차피 아래로 시작하는것도 있어서 이건 해주는게 좋을거같다.
# 시작 지점이 마이너스일때 체크하게 된다면 바로 오른쪽에 큰 수, 바로 아래쪽에 큰 수가 있는걸 넣어줄 수 없다.
# 행을 한번 쭉 더한다면 (시작열, 끝열이 정해져있으니, 그 행이 쓸모 없는지는 판단이 가능한 상황. 어차피 다음시행중에 그 행을 계산안하고 나머지를 계산하는것들이 존재한다.)

def find_max_submatrix(c_start, c_end):
    '''
    해당 지점으로 시작하는
    :param r_start: 시작 row
    :param c_start: 끝 row
    :return: 해당 지점에서 시작하는 것들중에 가장 큰걸 return
    '''
    max_matrix_sum = -9999999999
    for row_start in range(rows): # 시작 row
        temp_max = 0

        for row in range(row_start, rows):
            temp_max += sum(matrix[row][c_start:c_end])
            max_matrix_sum = max(max_matrix_sum, temp_max)
            if temp_max < 0:
                break
        else:
            max_matrix_sum = max(max_matrix_sum, temp_max)
    return max_matrix_sum




# column을 먼저 고정하고 시작하는 row를 바꿔가는 식. - 기둥 범위를 넓히고(end col)/ 옮기면서(start col) 탐색하는 방식.
max_val = -999999999
for column_start in range(columns): # 한번 더 타고 들어갈거라서 이렇게 해야됨.
    for column_end in range(column_start+1, columns+1):
        # for row_start in range(rows):
        #     for row_end in range(row_start + 1, rows):
        max_val = max(find_max_submatrix(column_start, column_end), max_val)
print(max_val)