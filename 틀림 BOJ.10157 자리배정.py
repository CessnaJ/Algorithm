# 0으로 차있는 기본 2차원 행렬을 만들고, 규칙에 맞게 (벽을 치거나, 뭔가를 만난다면 방향을 틀어서 시계방향으로 진행)
# 하는 방법으로 끝까지 진행한다. 그리고 2중 for loop 이용해서 해당 대기번호 사람이 완성 된 2차원 행렬에 존재하는지 확인한다.

total_col, total_row = list(map(int, input().split()))
target = int(input())
matrix = [[0]*total_col for _ in range(total_row)]

# 1.1 부터 시작하는데 따지고 보면 1.1은 x,y로 보면 최소/최소. but row/col으로 봤을때는 최대/최소다.

assign_idx = [total_row-1, 0]
# while문 사용해서 trigger걸고, 못채울때마다 방향을 바꾸는걸로 한다. (벽에 부딛히거나, 채워진 뭔가를 만나거나 조건 2개 걸어.)
# 방향을 맞추는 [dy, dx]들어있는 list를 만들어서 새로 돌때마다 방향을 바꾸는걸로 %4해서 무한루프 돌리는걸로 하면 됨.

direction_yx = [[-1, 0], [0, 1], [1, 0], [0, -1]] # row / col 짝지어놓은거니까 input이랑 축 전치됨. 헷갈리지말자.
crash = False
if total_row * total_col < target:
    print(0)
else:
    assignment = 1
    direction_order = 0
    for i in range(total_row * total_col):
        matrix[assign_idx[0]][assign_idx[1]] = assignment
        if assignment == target:
            print(assign_idx[1]+1, total_row - assign_idx[0])
            break
        # assign 해주고. # 아래는 벽에 부딛힌다면. 그리고 not을 써서 truthy로 인식되는 0이외의 assign된 객체와 만나게 된다면, 이라는 뜻. (건너기전에 돌다리 두들기는것.)
        if 0 <= assign_idx[0]+direction_yx[direction_order % 4][0] <= total_row-1 and 0 <= assign_idx[1]+direction_yx[direction_order % 4][1] <= total_col-1 \
                and not matrix[assign_idx[0]+direction_yx[direction_order % 4][0]][assign_idx[1]+direction_yx[direction_order % 4][1]]:

            assign_idx[0], assign_idx[1] = assign_idx[0]+direction_yx[direction_order % 4][0], assign_idx[1]+direction_yx[direction_order % 4][1]
        # 일단 이렇게 해서 방향에 맞게 idx 위치를 1번 더해서 바꿔줌.
        else:
            direction_order+=1
            assign_idx[0], assign_idx[1] = assign_idx[0] + direction_yx[direction_order % 4][0], assign_idx[1] + \
                                           direction_yx[direction_order % 4][1]

        assignment += 1

