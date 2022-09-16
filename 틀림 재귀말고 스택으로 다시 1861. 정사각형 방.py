# 풀기 전 생각! DFS/ BFS 이용해서 새롭게 visit하게 되는 경우 list에 넣어주고,
# 해당 탐색 알고리즘이 끝나면, len(list)해서 몇개 방문했는지 세준다.

def dfs(start, coor, visited, cnt):
    global startNsteps
    visited.append(coor)
    cnt += 1
    for k in range(4):
        drow = delta[k][0]
        dcol = delta[k][1]

        prev_row = coor[0]
        prev_col = coor[1]

        new_row = prev_row + drow
        new_col = prev_col + dcol
        if 0 <= new_row < N and 0 <= new_col < N:
            if [new_row, new_col] not in visited:
                if matrix[new_row][new_col] == matrix[prev_row][prev_col] + 1:
                    startNsteps.append([start, cnt])
                    dfs(start, [new_row, new_col], visited, cnt)



T = int(input())
startNsteps = []
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
for case in range(1, T+1):
    max_step = 0
    max_room_candi = []
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            count =0
            visited_coor = []
            dfs([i, j], [i, j], visited_coor, count)
    startNsteps.sort(key=lambda x: x[1], reverse=True)
    max_step = startNsteps[0][1]
    max_room_candi = []
    for [start, step] in startNsteps:
        if step == max_step:
            max_room_candi.append(start)
        else:
            break
    print(f'#{case} {max(max_room_candi)[0]} {max_step+1}')
