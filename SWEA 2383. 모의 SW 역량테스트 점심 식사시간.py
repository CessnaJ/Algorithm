# 어떻게 풀까?
# 1이 되는 좌표 싹 구함.
# 그 외의 숫자들 좌표 구함.
# 각 1이되는 좌표마다 여러개 계단으로 가는 시간을 nested list로 묶어서 가상좌표 계산을 함.
# 계단칸에 도착하면 1초 걸리고 k초가 더 걸리는데 3명까지만 된다고 했으니까 이 로직만 생각해서 계산할 수 있으면 경우의수에 따라서
# 돌려볼 수 있음.
# 계단마다 경우의 수 넣고 오름차순 정렬한다음에 끝나는 시간 정도인지 구할 수 있음. 마지막에 백트래킹 생각정도만 해주면 이 문제는 해결.

def find_coors():
    for row in range(matrix_size):
        for col in range(matrix_size):
            if not matrix[row][col]: # 0은 의미없으니 제낀다
                continue
            elif matrix[row][col] == 1: # 1은 사람이니까 저기 넣고
                person_coors.append((row, col))
            else: # 나머지는 계단이니까 좌표랑 같이 값을 넣어준다
                stair_coors.append((row, col, matrix[row][col]))


def calc_distance(person, stair):
    return abs(person[0] - stair[0]) + abs(person[1] - stair[1]) + 1 + stair[2]  # 1분 대기타니까 기본 1 더해줌.
    # return abs(person[0] - stair[0]) + abs(person[1] - stair[1])  # 1분 대기타니까 기본 1 더해줌.

T = int(input())

for case in range(1, T+1):
    matrix_size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
    person_coors = [] # 계산의 재료가 될 사람좌표 (row, col)
    stair_coors = [] # 계산의 재료가 될 계단좌표  (row, col, 계단값)

    find_coors()

    stair_a_length = stair_coors[0][2]
    stair_b_length = stair_coors[1][2]


    people_num = len(person_coors)
    stair_num = len(stair_coors)

    distance_to_each_floor = [[] for _ in range(people_num)] # 사람마다 각 계단으로 가면 얼마나 거리가 되는지. 계단 하나가 무지성 999인거 대비해서 다 해줘야할듯.
    # [ [1번남자a계단, 1번남자b계단], [2번남자a계단, 2번남자b계단], [3번남자a계단, 3번남자b계단] .... ]
    for i in range(people_num):
        for j in range(stair_num):
            distance_to_each_floor[i].append(calc_distance(person_coors[i], stair_coors[j]))

    # 와 계단 입구 2개구나 다행이다... DFS로 조합만들고 시뮬레이션 계산함수 만들어야하나 했는데 무지성 탐색 가능.. ㅠㅠ

    # 일단 backtracking해주는게 대기시간 고려 안하고 min값보다 저 무지성 합이 크면 그건 볼 필요가 없음.
    min_time = 9999999
    for i in range(1<<people_num): # 0 ~ 2^10 # 00000~00011~11111
        chose_stair_a = []
        chose_stair_b = []
        for j in range(people_num): # 0, 1
            if i & (1<<j):
                chose_stair_a.append(distance_to_each_floor[j][0])
            else:
                chose_stair_b.append(distance_to_each_floor[j][1])
        chose_stair_a.sort(reverse=True)
        chose_stair_b.sort(reverse=True)
        # 오름차순 정렬했으니 먼저 도착한 친구부터 들어갈거.
        if sum(chose_stair_a) > min_time or sum(chose_stair_b) > min_time:
            continue

        temp_a = 0
        temp_b = 0
        # on_stair_a = [0] + on_stair_a + [0, 0]
        # on_stair_b = [0] + on_stair_b + [0, 0]

        # for anchor in range(1, len(on_stair_a)-2):
        #     temp_a += on_stair_a[anchor]
        #     on_stair_a[anchor+1] -= on_stair_a[anchor]
        #     on_stair_a[anchor+2] -= on_stair_a[anchor]
        #     on_stair_a[anchor] = 0
        #
        # for anchor in range(1, len(on_stair_b)-2):
        #     temp_b += on_stair_b[anchor]
        #     on_stair_b[anchor + 1] -= on_stair_b[anchor]
        #     on_stair_b[anchor + 2] -= on_stair_b[anchor]
        #     on_stair_b[anchor] = 0
        # filter()
        len_a = len(chose_stair_a)
        len_b = len(chose_stair_b)
        on_stair_a = []
        on_stair_b = []
        # anchor = 1
        # 2개가 한번에 빠질 수도 있다.
        while chose_stair_a:

            candi = chose_stair_a.pop() # 내림차순이니까 가장 빨리온놈
            on_stair_a.append(candi)
            if len(on_stair_a) < 3: # 처음에 3칸 맞춰주기 위함, 한번에 2~3명 나가는거 생각.
                continue

            while on_stair_a[0]:
                for a in range(3): # 1씩 빼고
                    on_stair_a[a] -= 1
                temp_a += 1 # 시간 1 올림

            next_draw = True # 다음꺼 뽑아?
            while next_draw:
                if not on_stair_a[0]: # 0 되는지 검사. 근데 2,3명이 동시에 0이 될 수 있으니 while문으로 계속 봄. 2~3개 뽑아야할지 보려고
                    on_stair_a.pop(0) # 0 되었으니 뽑아냄 0이 된 친구가 있으니까 다음검사.
                else: # 맨 앞이 0이 아님.
                    next_draw = False # 이거 중단하고 다음꺼로 간다. # 다음회 되면 뺸만큼 뽑아넣겠지.

        while chose_stair_b:
            candi = chose_stair_b.pop()  # 내림차순이니까 가장 빨리온놈
            on_stair_b.append(candi)
            if len(on_stair_b) < 3:
                continue

            while on_stair_b[0]:
                for b in range(3):  # 1씩 빼고
                    on_stair_b[b] -= 1
                temp_b += 1  # 시간 1 올림

            next_draw = True
            while next_draw:
                if not on_stair_b[0]:  # 0 되면. 근데 2,3명이 동시에 0이 될 수 있음.
                    on_stair_b.pop(0)
                else:
                    next_draw = False

        # while chose_stair_b:
        #     candi = chose_stair_b.pop()
        #     on_stair_b.append(candi)
        #     if len(on_stair_b) < 3:
        #         continue



            #     on_stair_a==[0]*len_a and on_stair_b==[0]*len_b:
            # if not on_stair_a[anchor-1]:
            #     on_stair_a[anchor] += 1
            #



        if max(temp_a, temp_b) < min_time:
            min_time = max(temp_a, temp_b)

    # print(min_time)



    print(f'#{case} {min_time}')

