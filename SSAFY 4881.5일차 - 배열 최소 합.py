# 어떻게 풀것인가?
# 골라주는 함수를 쓸것. 만약에 이전에 골라져있는 row, col (set)안에 들어있다면 그 좌표는 넣지말고, min비교도 안함.

T = int(input())
row_set = set()
col_set = set()
def pick(row, col):

    if row in

for case in range(1, T+1):
    matrix_size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
    size_by_order = range(matrix_size)
    for i in size_by_order:
        for j in size_by_order:
            if i == j:
                continue
            for k in size_by_order:
                if k == j or k == i:
                    continue
                else:




    print(f'{case}')