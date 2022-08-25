# 그냥 종이에 그림 그리고 idx별로 규칙성 발견해서 풀었습니다.

T = int(input())

for case in range(1, T+1):
    size = int(input())
    matrix = [list(input().split()) for _ in range(size)]
    carton90 = []
    carton180 = []
    carton270 = []

    for i in range(size): # 90도 회전한거
        part90 = ''
        for j in range(size):
            part90 += matrix[size-1-j][i]
        carton90.append(part90)

    for i in range(size): # 180도 회전한거
        part180 = ''
        for j in range(size):
            part180 += matrix[size-1-i][size-1-j]
        carton180.append(part180)

    for i in range(size): # 270도 회전한거
        part270 = ''
        for j in range(size):
            part270 += matrix[j][size-1-i]
        carton270.append(part270)

    conversion_result = list(zip(carton90, carton180, carton270)) # 만든거 가로로 배열된거 세로로 바꾸고 unpacking해서 출력
    print(f'#{case}')
    for i in range(len(conversion_result)):
        print(*conversion_result[i])
