# 이거 chain식으로 풀어야된다. 이전숫자 base로 그 뒤의 dice의 방향을 맞춰나가는 식.
# 결국 각 dice의 아래쪽이 1번으로 오게 숫자를 정렬시키고,
# 근데 위아래를 정했다고 해서 측면이 정렬되는건 아니다. 4방향 모두 돌아갈 수 있다.
# 다 맞추고 나서 최대 합을 구하는것보다는, 일단 쌓아나가면서 최대가 되는 나머지 숫자를 점점 더해주면 될거같다.
# 그게 계산을 덜한다. 근데 제출해놓고 보니까 생각보다 실행시간 김.

def find_max_num(dice, top_index, bottom_index): # dice를 넣고, top_idx, bottom_idx를 넣으면 측면 최고 숫자를 반환해주는 함수.
    left_nums = []                               # bottom만 넣어도 알아서 반환해주게 만들 수 있겠지만 이렇게 했음.. ㅜ
    for i, j in enumerate(dice):                 # idx랑 숫자 따로 뽑아서 측면숫자에 맞는 value를 빈 list에 넣고 거기서 max값 찾음.
        if i in [top_index, bottom_index]:
            pass
        else:
            left_nums.append(j)
    return max(left_nums)


top_bottom_idx_corresponding_dict = {0: 5,
                                 1: 3,
                                 2: 4,
                                 3: 1,
                                 4: 2,
                                 5: 0}
dices = int(input())
dices_in_list = [list(map(int, input().split())) for _ in range(dices)]
max_side_sum = 0
tracking_target_number = 0
for i in dices_in_list[0]:        # 일단 첫째 dice의 bottom이 뭔지 모르니까 하나씩 넣는것.
    side_sum = 0                  # 이거를 for loop 밖에 둬서 refresh가 안되는 효과가 나서 20분 잡아먹음.
    tracking_target_number = i    # 가장 바깥 for loop이 첫 주사위의 모든 눈을 바닥으로 놓는 for loop임.
    bottom_idx = dices_in_list[0].index(i) # bottom idx를 찾으면 dict를 이용해서 대응되는 top_idx를 구할 수 있다.
    top_idx = top_bottom_idx_corresponding_dict[bottom_idx]
    side_sum += find_max_num(dices_in_list[0], top_idx, bottom_idx) # 측면 최고숫자 구함.
    tracking_target_number = dices_in_list[0][top_idx]              # 직전 dice의 top숫자를 다음 dice의 bottom으로 놓기 위함.
    for j in dices_in_list[1:]:
        bottom_idx = j.index(tracking_target_number)                # 진행 방식 위랑 완전 동일.
        top_idx = top_bottom_idx_corresponding_dict[bottom_idx]
        side_sum += find_max_num(j, top_idx, bottom_idx)
        tracking_target_number = j[top_idx]
    if side_sum > max_side_sum:                                     # 1번 dice 방향 바꿔가면서 뭐가 최선인지 보는것.
        max_side_sum = side_sum
print(max_side_sum)