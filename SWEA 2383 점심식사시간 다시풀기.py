# 어떻게 풀까?
# 1이 되는 좌표 싹 구함.
# 그 외의 숫자들 좌표 구함.
# 각 1이되는 좌표마다 여러개 계단으로 가는 시간을 nested list로 묶어서 가상좌표 계산을 함.
# 계단칸에 도착하면 1초 걸리고 k초가 더 걸리는데 3명까지만 된다고 했으니까 이 로직만 생각해서 계산할 수 있으면 경우의수에 따라서
# 돌려볼 수 있음.
# 계단마다 경우의 수 넣고 오름차순 정렬한다음에 끝나는 시간 정도인지 구할 수 있음. 마지막에 백트래킹 생각정도만 해주면 이 문제는 해결.

# 걍 시뮬레이션 돌릴걸 하..


def find_coors():
    for row in range(matrix_size):
        for col in range(matrix_size):
            if not matrix[row][col]:  # 0은 의미없으니 제낀다
                continue
            elif matrix[row][col] == 1:  # 1은 사람이니까 저기 넣고
                person_coors.append((row, col))
            else:  # 나머지는 계단이니까 좌표랑 같이 값을 넣어준다
                stair_coors.append((row, col, matrix[row][col]))


def calc_distance(person, stair):
    return abs(person[0] - stair[0]) + abs(person[1] - stair[1]) + stair[2] + 1  # 1분 대기타니까 기본 1 더해줌.(3명 꽉 안찰때만 1 더함)
    # return abs(person[0] - stair[0]) + abs(person[1] - stair[1])  # 1분 대기타니까 기본 1 더해줌.


def get_stair_time(arr, k):
    if not arr:
        return 0
    i = 3
    while i < len(arr):
        if arr[i] < arr[i-3] + k:
            arr[i] = arr[i-3] + k
        i += 1
    return arr[-1] + k



T = int(input())

for case in range(1, T + 1):
    matrix_size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
    person_coors = []  # 계산의 재료가 될 사람좌표 (row, col)
    stair_coors = []  # 계산의 재료가 될 계단좌표  (row, col, 계단값)

    find_coors()

    stair_a_length = stair_coors[0][2]
    stair_b_length = stair_coors[1][2]

    people_num = len(person_coors)
    stair_num = len(stair_coors)

    distance_to_each_floor = [[] for _ in range(people_num)]  # 사람마다 각 계단으로 가면 얼마나 거리가 되는지. 계단 하나가 무지성 999인거 대비해서 다 해줘야할듯.
    # [ [1번남자a계단, 1번남자b계단], [2번남자a계단, 2번남자b계단], [3번남자a계단, 3번남자b계단] .... ]
    for i in range(people_num):
        for j in range(stair_num):
            distance_to_each_floor[i].append(calc_distance(person_coors[i], stair_coors[j]))

    # 와 계단 입구 2개구나 다행이다... DFS로 조합만들고 시뮬레이션 계산함수 만들어야하나 했는데 무지성 탐색 가능.. ㅠㅠ

    # 일단 backtracking해주는게 대기시간 고려 안하고 min값보다 저 무지성 합이 크면 그건 볼 필요가 없음. - 이거떄문에 오히려 더 틀림. 더 잘 분배되는 경우도 있다.
    min_time = 9999999
    for i in range(1 << people_num):  # 0 ~ 2^10 # 00000~00011~11111
        on_stair_a = []
        on_stair_b = []
        for j in range(people_num):  # 0, 1
            if i & (1 << j):
                on_stair_a.append(distance_to_each_floor[j][0])
            else:
                on_stair_b.append(distance_to_each_floor[j][1])
        on_stair_a.sort()
        on_stair_b.sort()
        # 오름차순 정렬했으니 먼저 도착한 친구부터 들어갈거.
        # if sum(on_stair_a) > min_time or sum(on_stair_b) > min_time:
        #     continue

        # on_stair_a = [6,7,8]
        # on_stair_b = [8,9,9]


        temp_a = 0
        temp_b = 0
        on_stair_a = [0] + on_stair_a + [0, 0, 0]
        on_stair_b = [0] + on_stair_b + [0, 0, 0]

        print(on_stair_a)
        print(on_stair_b)

        temp_a = get_stair_time(on_stair_a, stair_a_length)
        temp_b = get_stair_time(on_stair_b, stair_b_length)

        # for anchor in range(1, len(on_stair_a) - 3):
        #     temp_a += on_stair_a[anchor]
        #     on_stair_a[anchor + 1] -= on_stair_a[anchor]
        #     on_stair_a[anchor + 2] -= on_stair_a[anchor]
        #     on_stair_a[anchor] = 0
        #     if on_stair_a[anchor + 2] == 0 and on_stair_a[anchor + 3] != 0:
        #         on_stair_a[anchor + 3] -= 1
        #     elif on_stair_a[anchor + 1] == 0 and on_stair_a[anchor + 2] != 0:
        #         on_stair_a[anchor + 2] -= 1
        #
        #
        # for anchor in range(1, len(on_stair_b) - 3):
        #     temp_b += on_stair_b[anchor]
        #     on_stair_b[anchor + 1] -= on_stair_b[anchor]
        #     on_stair_b[anchor + 2] -= on_stair_b[anchor]
        #     on_stair_b[anchor] = 0
        #     if on_stair_b[anchor + 2] == 0 and on_stair_b[anchor + 3] != 0:
        #         on_stair_b[anchor + 3] -= 1
        #     elif on_stair_b[anchor + 1] == 0 and on_stair_b[anchor + 2] != 0:
        #         on_stair_b[anchor + 2] -= 1


        if max(temp_a, temp_b) < min_time:
            min_time = max(temp_a, temp_b)

    # print(min_time)

    print(f'#{case} {min_time}')