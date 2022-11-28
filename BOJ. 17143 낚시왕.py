'''

격자판 r x c

r -> row
c -> column


shark - 크기 / 속도 가지고 있음.

처음 낚시왕 위치  - 0,0
1초동안 일어날 일 다음과 같음.
    1. 낚시왕이 오른쪽으로 1칸 이동 -> col + 1
    2. 낚시왕이 있는 column에 있는 상어중에서 땅와 가장 가까운(row의 abs가 작음) 상어를 잡음(잡으면 matrix에서 상어 사라짐)
    3. 상어 이동

상어는 input으로 주어진 속도로 이동.
속도 -> 칸/초
상어가 이동하려고 하는 칸이 edge를 넘으면 방향 '반대'로 바꿔서 speed유지

1 - 위로이동        row -
2 - 아래로이동      row +

3 - 우로이동        col +
4 - 좌로이동        col -

1칸에 상어 2마리 겹치면 큰 상어가 나머지 다 잡아먹음.
예시보니 잡아먹었다고 크기가 가산되지는 않음.

낚시왕이 잡은 상어크기의 합을 출력. (0~col까지 순차적으로 가서 끝내게됨.)
'''


given_row, given_col, sharks = map(int, input().split())
bucket = 0


# matrix = [[[0, 0, 0] for x in range(given_col)] for y in range(given_row)]
# 위대로 하면 무조건 시간초과



# row, col, speed, direction, size 가 각각 들어간다.
sharks_list = [list(map(int, input().split())) for _ in range(sharks)]



for turn in range(given_col):
    # 정렬 후 뽑는게 먼저.
    list_len = len(sharks_list)
    sharks_list.sort(key=lambda x: (x[1], x[0]))  # x[1] col기준으로 asc 하고나서 그 후순위 정렬을 x[0] row asc로 삼는것.

    for i in range(list_len):
        if sharks_list[i][1] == turn:
            bucket += sharks_list[i][4]
            sharks_list.pop(i)
            break
            # 할거 다 했으니까 끝내기. 정렬 후 처음 마주친 col의 값이 가장 작은 row일거니까 이렇게.


    for j in range(len(sharks_list)):
        if sharks_list[j][3] <= 2:
            sharks_list[j][0] =



    # matrix[row][col] = [speed, direction, size]
# row, col, speed, direction, size


# # 어부턴, 상어턴으로 나뉨.
# for fisherman_col in range(given_col):
#     # 어부 턴
#     for fisherman_row in range(given_row):
#         if matrix[fisherman_col][fisherman_col] != [0, 0, 0]:
#             bucket += matrix[fisherman_col][fisherman_col][2]
#             matrix[fisherman_col][fisherman_col] = [0, 0, 0]
#             break

