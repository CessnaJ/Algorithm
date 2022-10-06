import sys
input = sys.stdin.readline
from collections import deque
length, width, height = map(int, input().split()) # 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100
# 1 - 익은 토마토
# 0 - 안익은 토마토
# -1 - 빈칸 (진출불가)

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]

def tomato_check():
    global count
    for z in range(height):
        for y in range(width):
            for x in range(length):
                if matrix[z][y][x] == 0:
                    count = -1
                    return


def isvalid(newZ, newY, newX):                                                # 유효성 검사
    if not (0 <= newX < length and 0 <= newY < width and 0 <= newZ < height): # 경계 침범시 False
        return False

    if matrix[newZ][newY][newX] in [-1, 1]:                                   # 썩으면 막히고, 이미 익었으면 중복호출없도록 False
        return False
    return True


matrix = [[list(map(int, sys.stdin.readline().split())) for y in range(width)] for z in range(height)]

Q = deque()
for z in range(height):
    for y in range(width):
        for x in range(length):
            if matrix[z][y][x] == 1:
                Q.append((z, y, x, 0)) # 0은 카운트

while Q:
    z, y, x, count = Q.popleft()
    matrix[z][y][x] = 1
        for dir in range(6):
            tempz = z + dz[dir]
            tempy = y + dy[dir]
            tempx = x + dx[dir]
            if isvalid(tempz, tempy, tempx):
                Q.append((tempz, tempy, tempx, count+1))

tomato_check() # 0이 있으면 count변수를 -1로 바꿔주는 함수. 0을 발견하면 return을 해서 끝내기.
print(count)