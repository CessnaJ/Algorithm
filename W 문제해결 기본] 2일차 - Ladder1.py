# 오늘도 굉장히 의미없는가정 ( 첫번째줄이 가로줄이면 어떻게 하지?)를 생각하며 이상한 뻘짓을 했습니다. 문제를 잘 읽어야합니다. 근데 어차피 이렇게 해도 문제는 풀리니까 그냥 갑니다.

given_ladder = [list(map(int, input().split())) for _ in range(100)]

# 사다리 게임 역순으로 가서, 시작점의 col 좌표 return
# 매 실행마다 좌우 있는지 탐색(좌우를 봤을때 list의 edge를 벗어나면 그쪽은 탐색하지 않는다.)
# 있다면 좌,우로간다.
given_ladder = [list(map(int, input().split())) for _ in range(100)]
trace_marking = [[0]*100 for _ in range(100)]

once_proceed_to_left = False
once_proceed_to_right = False
for i in given_ladder[99]: # for loop으로 start 위치 찾기.
    if i == 2:
        row, col = 99, i
        new_position = [row, col]
while trace_marking[row] != 0: # new_position의 trace를 계속 marking하게 됨. marking한 postion이 row 0가 되면 위치 출력하고 종료할것임.
    if once_proceed_to_left: #왼쪽으로 가던 중이었는지 체크하고 왼쪽이 끝날때까지 계속 이동. (사다리의 가로줄을 탄다는 의미)
        if given_ladder[row][col - 1] == 1: # 모멘텀 있음 + 옆으로 갈 수 있음.
            col = col - 1
            trace_marking[row][col] = 1 # trace_marking해주는 다른 layer에 기록해줌.
        else: # 모멘텀 있음. 막힘.
            once_proceed_to_left = False # 한번 옆으로 진행이 불가능하게 되면 계속 진행하려는 모멘텀도 없애주기 위함.
    elif once_proceed_to_right: #오른쪽으로 가던 중이었는지 체크하고 왼쪽이 끝날때까지 계속 이동. (사다리의 가로줄을 탄다는 의미)
        if given_ladder[row][col + 1] == 1: # 모멘텀 있음. + 오른쪽으로 감.
            col = col + 1
            trace_marking[row][col] = 1
        else: # 모멘텀 있음 + 막힘
            once_proceed_to_right = False
    else: #가로줄 타던중이 아니었으니.. (그럼 처음 시작할때부터 바로 가로줄 타는경우는 어떻게하나? 이거는 직전이 가로줄이었니? 라는 flag를 또 만들어주면 됨.) # 모멘텀 없음.
        if (trace_marking[row][col-1] == 1) or (trace_marking[row][col+1] == 1): # 기존에 다른 layer에 흔적을 marking하고 있었기때문에 양 옆에 흔적이 있으면 (위 조건문에서 모멘텀이 사라지고, 흔적이 있다면 이제는 위로 올라가야한다는뜻.)
            row = row -1
            trace_marking[row][col] = 1



                current_position




    while new_position[row] != 0:

        current[99]



'''
내 로직.
좌우가 제일 우선이다. (좌우가 있다면 일단 간다!) 그 다음 스텝으로(once moved to left/right direction -> proceed until encountered 0 block. (탐색, 이동))
상/하 중에서는 위로 가는게 우선이다.

current_position
new_position
을 만들어서 끼워넣고 둘을 비교하는 과정을 거친다. 좌우가 없을시 상으로 움직인다.
'''
