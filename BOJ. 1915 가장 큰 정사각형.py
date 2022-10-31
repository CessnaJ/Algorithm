# dp적으로 풀어보자. 1x1 확인해서 정사각형 만족하면 1 저장. 2x2확인해서 만족하면 4 저장 이런식으로 쭉쭉..

# 저장 할 매트릭스 따로 또 만들어 줘야함.
from sys import stdin

rows, cols = map(int, input().split())

matrix = [list(map(int, list(stdin.readline().strip()))) for _ in range(rows)]
zip_matrix = list(zip(*matrix))


dp_matrix = [[0]*cols for _ in range(rows)]

for row in range(rows):      # 기준 row
    for col in range(cols):  # 기준 col
        if matrix[row][col]: # 기준좌표에서 시작하겠다.
            cycle = 1        # 시작할때 기본 사이클값
            while cycle:     # 사이클이 0이 아니라면 반복
                for i in range(cycle+1): # 사이클
                    if row+i < rows and col+i < cols and matrix[row+cycle-1][col+i] and matrix[row+i][col+cycle-1]:
                        pass
                    else:
                        dp_matrix[row][col] = cycle+0
                        cycle = 0
                        break
                else:
                    cycle += 1

max_size = 0
for i in range(rows):
    for j in range(cols):
        max_size = max(max_size, dp_matrix[i][j])

print(*dp_matrix, sep='\n')
print(max_size**2)
