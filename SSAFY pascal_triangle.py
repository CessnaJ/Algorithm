T = int(input())

def pascal_triangle(n):             # 함수 생성. reucrsive로 몇번째 줄을 만들지 parameter로 받음.
    if n == 1:                    # recursive의 end point 지정.
        return [1]
    else:                           # 아니라면.
        new_row = [1]               # 일단 맨 왼쪽에 1 넣기
        last_row = pascal_triangle(n-1)
        for i in range(len(last_row)-1):      # idx 2개 더해서 밀어넣기
           new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]              # 마지막에도 1 넣기
    return new_row

for case in range(1, T+1):
    total_row = int(input())
    for i in range(1, total_row + 1):
        print(*pascal_triangle(i))
# print(*pascal_triangle(4))