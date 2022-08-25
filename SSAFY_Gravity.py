# 낙차를 어떻게 구할까.. 2차원 matrix를 만들어서 전치를 할까 하다가 이 문제를 심플하게 푸는게 목적이라는 생각이 들어 다시 생각해보았다.
# 결국 90도를 틀어서 떨어지는 높이를 측정한다는것은, 해당 높이를 기준으로 그 기준높이 이상의 기둥이 오른쪽에 몇개가 있냐에 따라 결정된다는 것.
# 최대 낙차만 구하면 된다고 했지, 좌표를 구하라는 말이 없었기 때문에 원하는 정보만 추출하겠습니다.
# 항상 100칸이라고 했음. 그리고 input으로 보여준 예시 보니까 빈 공간에 0도 줌. (단순한 문제라서 칸이 달라도 문제 난이도가 올라가지 않습니다.)
box_tower_list = list(map(int, input().split())) # list로 주어진 box_tower의 높이들을 받습니다.
max_fall_off_height = 0
for i in range(100): # 낙차를 구할 기준이 되는 index를 i라고 봅니다.
    count = 0        # 기준box_tower가 바뀔 때 마다 count가 refresh 되는게 옳습니다.
    fall_off_height = 0 # fall_off_height도 동일.
    for j in range(i+1, 100): # i의 오른쪽 기둥부터 brute force 탐색 진행합니다.
        if box_tower_list[j] >= box_tower_list[i]: # idx j를 가진 twr가 기준점idx 기둥높이 이상이면.. 90도 돌렸을때 밑에 깔리니까 count 1개씩 올려줍니다.
            count += 1
    fall_off_height = 100 - (i + count) # 최대치가 100이 될거고, index에 맞춰서 오른쪽으로 1칸씩 가면 최대 높이도 그만큼 줄어듬 + 밑에 깔리는 개수에 맞춰서 낙차 줄어듬.
    if fall_off_height > max_fall_off_height: # 최대치 갱신되면 max_fall_off_height로 갱신시켜줍니다.
        max_fall_off_height = fall_off_height

print(max_fall_off_height) #SWEA 문제가 있었다면 규격에 맞추었겠지만 그게 아니라서 1번만 하고 출력하는걸로 했습니다.