adj_matrix[start][end] = 1
adj_matrix[end][start] = 1 # 양방향 그래프니까!!
Q = [1] # 맨처음 시작점은 1번 포도알
visited = [] # 궤적 기록용
while Q: # 큐가 빌때까지 돌아라!
    current = Q.pop(0) # 우선 큐에서 현재 위치 "앞에서부터" 뽑고,
    if current not in visited: # 방문하지 않은 곳이라면,
        visited.append(current) # 방문했다고 체크해줌
    for destination in range(V+1): # current 입장에서 어디로 갈 수 있는지 모조리 체크
        if adj_matrix[current][destination] and destination not in visited: # 갈수있고 + 방문 안했으면!
            Q.append(destination) # 다음 갈 곳으로 큐에 저장
print('이동경로:', *visited)

---------------------------------------------------------------------------------------------------------------
row_limit = 3  # 경계선언
col_limit = 3

grid = [[1, 2, 3],
        [0, 9, 8],
        [1, 0, 1]]

# Initialize direction vectors
dRow = [0, 1, 0, -1]  # row방향 delta 선언
dCol = [-1, 0, 1, 0]  # col방향 delta 선언
visited = [[False for i in range(3)] for j in range(3)]  # visited matrix 선언


def isValid(row, col):  # 방문하기 전에 방문가능한지 T/F로 보여주기 위한 함수.
    global row_limit
    global col_limit
    global visited
    # If cell is out of bounds
    if (row < 0 or col < 0 or row >= row_limit or col >= col_limit):  # 경계를 넘었다면
        return False
        # If the cell is already visited
    if (visited[row][col]):  # row/col 넣어서 방문처리 되어있다면
        return False
        '''이 부분에 제한사항을 또 끼워넣을 수 있다. 미로라면 값이 0이라면, 1이라면 이런식으로.'''
    return True


def DFS(row, col, grid):  # 함수 선언을 통해 해당 기준 row/col부터 델타탐색을 할 수 있음.
    global dRow
    global dCol
    global visited

    stack = [[row, col]]

    while stack:
        current = stack.pop()
        row = current[0]
        col = current[1]

        if (isValid(row, col) == False):
            continue

        visited[row][col] = True  # 방문처리하기
        print(grid[row][col], end=" ")  # 델타탐색하면서 액션이 이루어지는 부분.

        # Push all the adjacent cells
        for i in range(4):  # 4방향 넣어주기. 막 넣어도 어차피 pop되면서 isValid에 걸리게 된다.
            adjx = row + dRow[i]  # 가장 최근에 넣은게 또 4방탐색을 하면서 쭉쭉쭉 나아가게 해준다.
            adjy = col + dCol[i]  # 그래서 DFS임.
            stack.append([adjx, adjy])