# idx를 통해서 왼쪽, 오른쪽 탐색을 시작해야하니까.. 아마 쉽지않다. max가 되는 키를 중심으로 해서 양쪽으로
# 싸나가는 식으로 해야될거같음. 왼쪽이라 치면, 한번 탐색 쭉~ 해서 왼쪽에 나보다 키 큰애가 없어야 저장되는식.
# (저장될떄는 좌표랑 키를 저장하는 list를 만듬. 왼쪽 오른쪽에. 그 다음에 넓이를 구하면 된다.)
# 아 근데 dict로 1000개 다하면 싹 탐색해버리니까 안되겠다. list 속 list로 해결해야될듯. 그리고 그 다음에 dict를 그 기반으로 만들어서 계산해주면 될거같음.

x_height_corresponding_dict = {}
sorted_x_height_dict = {}
number_of_column = int(input())
max_height = 0
x_on_max_height = 0
for i in range(number_of_column):
    L, H = map(int, input().split())
    if H > max_height:                 # 어차피 dict 만들면서 돌아가니까 이걸로 돌린다. 할 때 하는게 효율적이고 편함.
        max_height = H                 # max height를 찾음
        x_on_max_height = L            # max height의 x좌표를 찾음
    x_height_corresponding_dict[L] = H # dict를 key 순서로 ascending 정렬해서 미리 찾은 max의 위치 기반으로 탐색 시작할것임.

sorted_x_height_list = sorted(x_height_corresponding_dict.items()) # list로 바뀌는건 맘에 안들지만 어차피 왼쪽으로 쭉 탐색할거라서 괜찮다..
for a, b in sorted_x_height_list:
    sorted_x_height_dict[a] = b
# 자 여기까지 했으니까 중간정리. 난 무엇을 구했나? L 순서대로 정렬이 된 L을 key로 가지고 H를 value로 가지는 dict인 sorted_x_height_dict
# 그리고 max기둥을 가리키는 L과 H가 들어있는 max_height, x_on_max_height, 그리고 list slicing이 가능한 sorted_x_height_list
# 아마 넓이니까 오른쪽탐색하면서는 1을 가로길이에 더해서 높이랑 곱하는 식으로 나갈거같음.
pivot_idx_l = 0
pivot_idx_r = 0
pivot_height_l = H + 0
pivot_height_r = H + 0

for j in range(len(sorted_x_height_list)): # max를 알고 있기에(하지만 이 경우 좌측의 max가 될것이다. 동일한 키의 max값이 3~4개 일수도 있다는걸 생각해보자.) 그걸 기준으로 pivot으로 삼아서 좌우측 탐색을 이어나갈것이다.
    if sorted_x_height_list[j][1] == H:    # 넓이를 구하는게 목적임. 좌측으로는 그냥 정석대로 해주면 되는데, 기둥 하나의 기본 너비가 1이니까 오른쪽 한칸은 max키만큼 더 해주고, 그만큼 최우측에서 1칸씩 밀려준다고 보면 된다. max높이만큼 더하고, min 높이만큼 빼면 됨)
        pivot_idx_l = j + 0 # 똑같은 포인터 안가리키게..
        pivot_idx_r = j + 0
area_sum_on_l = 0
area_sum_on_r = 0

for k in range(pivot_idx_l-1, -1, -1): #왼쪽 탐색해나가면서 넓이를 더해줍니다.
    if sorted_x_height_list[k][1] >= pivot_height_l:
        pivot_height_l = sorted_x_height_list[k][1]
        pivot_idx_l = sorted_x_height_list[k][0]
        area_sum_on_l += 0 # 이거 포기.. 꼬여서 못하겠음..

# 접근방법 좋은데 다음번에 다시 풀도록 하자.



print(sorted_x_height_dict)

# print(sorted_x_height_dict)
# print(x_height_corresponding_dict)
# my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}

# sorted_x_height_dict = sorted(x_height_corresponding_dict.items()) # 이거 내가 푼거 아님. 공부 다시. [('a', 1), ('b', 2), ('c', 3), ('d', 2), ('e', 1)]



# default_dict_keys = list(range(999))
# col_height_corresponding_dict= dict.fromkeys(default_dict_keys, 0)

