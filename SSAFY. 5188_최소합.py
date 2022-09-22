from collections import deque
import time
T = int(input())

start = time.time()
def traverse(row_col_val):
    row = row_col_val[0]
    col = row_col_val[1]
    prev_value = row_col_val[2]
    value = prev_value + matrix[row][col]

    if row != N-1:
        working.append([row+1, col, value])
    if col != N-1:
        working.append([row, col+1, value])
    if row == N-1 and col == N-1:
        finished.append(value)


for case in range(1, T+1):
    N = int(input())

    working = deque()
    working.append([0, 0, 0])
    finished = []
    matrix = [list(map(int, input().split())) for _ in range(N)]

    while working:
        traverse(working.popleft())

    print(f'#{case} {min(finished)}')

end = time.time()
print(end-start)