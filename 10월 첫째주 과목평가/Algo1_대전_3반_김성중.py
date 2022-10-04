drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]
# 0은 빈 땅    (공격가능, 변환가능)
# 1,2은 장애물 (공격불가, 변환불가, 통과불과)
# 공격된거는 3으로 마킹하고 0 개수 셀거임.


def isvalid(newrow, newcol):
    if not(0 <= newrow < map_size and 0 <= newcol < map_size): # 맵을 벗어난다면
        return False
    if matrix[newrow][newcol] in [1, 2]: # 장애물이거나, 방어탑이라면
        return False
    return True


def marking(row, col, direction):
    global matrix
    new_row = row + drow[direction]
    new_col = col + dcol[direction]
    if isvalid(new_row, new_col): # 가능하면
        matrix[new_row][new_col] = 3 # 마킹하고
        marking(new_row, new_col, direction) # 그 방향으로 더 타고 들어가
    else:
        return


T = int(input())

for case in range(1, T+1):
    map_size = int(input()) # 5~20
    matrix = [list(map(int, input().split())) for _ in range(map_size)] # 원래 맵 받아오기
    for i in range(map_size):  # i,j 하나씩 탐색해가면서 2가 아니라면(포대가 아니면) 다음 좌표로 넘기고
        for j in range(map_size):
            if not matrix[i][j] == 2:
                continue
            else:  # 포대라고 한다면
                for dir in range(4): # 4방향으로 각각 쭉 타고 들어가기(발사)
                    marking(i, j, dir)

    count = 0
    for x in range(map_size):  # 색칠 다 했으니까 0 셀거임.
        for y in range(map_size):
            if matrix[x][y] == 0:
                count += 1

    print(f'#{case} {count}')