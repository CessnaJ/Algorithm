# 어떻게 풀것인가? 원형큐 이용. str형태의 list를 각변의 개수만큼 돌려본다.
# 16진수로 받는 int함수 이용. 모든 경우의 수 넣어보면서 desc정렬 반복.
# k번째로 원하는 숫자를 뽑으라 하니, idx접근으로 출력 해주면 됨. 끝~
# 숫자 개수를 4로 나눈게 한변에 주어지는 숫자들의 개수.
# 숫자들의 개수 -1번만큼 돌릴수있다.

T = int(input())

for case in range(1, T+1):
    N, K = map(int, input().split())
    nums_per_line = int(N/4)
    # total_rotation = nums_per_line-1
    circle_Q = list(input()) # str들로 하나하나 쪼개서 list로 받고싶다~ 합치는건 join 이용해서 합치면 되겠지?
    side_nums = set()
    for rotation in range(nums_per_line):

        for i in range(3):
            start = i*nums_per_line
            end = i*nums_per_line + nums_per_line
            each_side_listed = circle_Q[start+rotation: end+rotation]
            each_side_str = ''.join(each_side_listed)
            each_side_num = int(each_side_str, 16)
            side_nums.add(each_side_num)
            # print(each_side_num)
        last_side_listed = circle_Q[3*nums_per_line+rotation:] + circle_Q[:rotation]
        last_side_str = ''.join(last_side_listed)
        last_side_num = int(last_side_str, 16)
        side_nums.add(last_side_num)
        # print(f'im the last {last_side_num}')
    sorted_nums = sorted(list(side_nums), reverse=True)
    # print(sorted_nums)

    print(f'#{case} {sorted_nums[K-1]}')