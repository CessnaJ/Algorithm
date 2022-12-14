height, length = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(height)]

start = (height-1, 0)
end = (height-1, length-1)

submatrix1 = [[0]*length for _ in range(height)]
submatrix2 = [[0]*length for _ in range(height)]

submatrix1[height-1][0] = matrix[height-1][0] # 상승 첫칸 채우기
submatrix2[0][length-1] = matrix[0][length-1] # 하강 첫칸 채우기

for alt in range(1, height): # 첫 열 채우기
    submatrix1[height-alt][0] = matrix[height-alt][0] + submatrix1[height+1-alt][0]
    submatrix2[height-alt] = matrix[height-alt][0] + submatrix2[height-alt+1][0]

for altitude in range(height):
    for distance in range(length):
        submatrix1[altitude][distance] = submatrix1[altitude][distance] + max()


# 위쪽 오른쪽으로 누적합 채워나가기 (matrix값, 누적합 matrix의 왼쪽,아래쪽과 비교해서 더 큰거랑 더해줌)
# 왼쪽 위로 누적합 채워나가기 (matrix값, 누적합matrix의 오른쪽, 아래쪽과 비교해서 더 큰거랑 더해줌)