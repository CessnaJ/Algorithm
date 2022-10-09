# 구슬은 N번 쏠 수 있다.
# Width, Height 2차원 배열 주어짐(벽돌정보)
# 0은 빈공간 의미. 그 외 숫자는 벽돌(1-9)을 의미.
# 해당 벽돌이 타격되면, 상하좌우로(적힌수 -1)만큼 같이 제거 됨.
# 연쇄 작업으로 박살날게 모두 지정되면 그제서야 삭제가 되고, 밑으로 채워나가는 작업을 진행한다.

# 여기까지는 쉬움

# 문제는 N개의 벽돌을 떨어뜨려서 최대한 많은 벽돌을 제거하려고 할 때, 남은 벽돌의 개수를 구하는것!
# 그리디로 갈까 아니면 경우의 수로 갈까? -> 문제의 조건을 보고 N이 몇개인지 한번 보자~

# 제약사항을 보면 N이 기껏해야 4개밖에 안된다. 재귀를 이용해서 name space를 분리하고, 각 경우의 수에 대해서 진행해봐도 될거같다.
# width가 12개니까 12^4의 경우의 수가 나올테니. 1500개정도의 재귀호출을 하면 될것이다.

from collections import deque

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

def organize(matrix_before): # 다 하고나서 밑으로 빼주는 함수 (해당 namespace에 있는 matrix에 대해 action만 이루어질것이다.)
    # 스택 이용해서 쭈욱 채운 매트릭스 새로 만들어서 반환해버리기.
    organized_matrix = [[0]*width for _ in range(height)]
    stack = []
    for col in range(width):
        for row in range(height):
            if matrix_before[row][col]:
                stack.append(matrix_before[row][col])
        else:
            row = height - 1
            while stack:
                organized_matrix[row][col] = stack.pop()
                row -= 1
    return organized_matrix




def chain_crack(matrix, col, trial):
    global visited
    Q = deque() # 연쇄 폭발은 depth를 안써야하니 iteration으로 해결

    if trial == N+1: # 반환해서 끝내주기 위한 basecase/ 뭘 반환 -> 남은 개수
        cnt = 0
        for jj in range(width):
            for ii in range(height):
                if matrix[ii][jj]:
                    cnt += 1
        count_list.append(cnt)

    coor = find_start_coor(matrix, col)
    Q.append(coor)


    while Q:
        r, c = Q.popleft()
        if not r and not c:
            return
        num = matrix[r][c]
        matrix[r][c] = 0
        for dir in range(4):
            for distance in range(1, num): # 이러면 1일때는 안넣음. -1까지만 넣게 될거고.
                new_row = r + drow[dir] * distance
                new_col = c + dcol[dir] * distance
                if 0 <= new_row < height and 0 <= new_col < width and not visited[new_row][new_col]:
                    Q.append((new_row, new_col))
    # 여기까지 하면 일단 그 trial의 0 만들기는 성공~

    organized_matrix = organize(matrix) # 다 했으면 정리하고

    for j in range(width): # 다음 시행으로 들어간다.
        chain_crack(organized_matrix, j, trial+1)



def find_start_coor(given_matrix, col):
    for row in range(height):
        if given_matrix[row][col]:
            return row, col, # tuple형으로 시작좌표 반환.
    else:
        return 0,0,




count_list = []
T = int(input())

for case in range(1, T+1):
    N, width, height = map(int, input().split())
    block_matrix = [list(map(int, input().split())) for _ in range(height)]
    # blocks_left = 999999
    visited = [[False]*width for _ in range(height)]
    for i in range(width):
        # temp =
        chain_crack(block_matrix, i, 1)
        # blocks_left = min(temp, blocks_left)
        # break # 찾아서 갱신시킬거고, 찾았으면 더 내려가면 안되니까. break해서 다음 경우의 수를 본다.

    print(count_list)
    print(f'# {min(count_list)}')