# row 기준 col탐색 후 , col 기준 row탐색. 그리고 작은 square 탐색.
# 각 숫자가 하나씩 있는지를 찾으라는말은, 각 검증 list의 각 원소를 봤을때, 만약에 그 list안에 1~9 중 1개라도 없으면 문제가 있다는것.
T = int(input())
def verify(checklist):
    dummy = []
    one_to_nine = list(range(1, 10))
    for a in checklist:
        dummy.append(a)

    if sorted(dummy) != one_to_nine:
        return False
    else:
        return True

all_done = True

for case in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    for row in sudoku:
        if not verify(row):
            print(f'#{case} {0}')
            all_done = False
            break
    if not all_done:
        continue

    sudoku_t = list(zip(*sudoku))
    for col in sudoku_t:
        if not verify(col):
            print(f'#{case} {0}')
            all_done = False
            break
    if not all_done:
        continue

    anchor = [0, 3, 6]
    for row in anchor:
        for col in anchor:
            small_square = []
            for i in range(3):
                for j in range(3):
                    small_square.append(sudoku[row+i][col+j])
                    if not verify(small_square):
                        print(f'#{case} {0}')
                        all_done = False
                    if not all_done:
                        break
                if not all_done:
                    break
            if not all_done:
                break
        if not all_done:
            break



    if all_done:
        print(f'#{case} {1}')
