T = int(input())
multiply_check = [4, 6, 7, 9, 11]

for case in range(1, T+1):
    total_gems, target_value = map(int, input().split()) # 보석개수(3~20), 근접해야되는 예산(0~200)(블랙잭룰) # 배낭문제지만 bruteforce로 풀것임.
    gems = list(map(int, input().split()))
    unusable_gems = set()
    for item in gems: # 여러번 제거되면 value error 날 수 있음. set에 거를거 한번에 모아서 나중에 빼주는게 안전.
        for check in multiply_check:
            if not item % check: # 나머지 0이면 쓸 수 있는 보석이니까 다음 아이템으로 넘기고, 완주하면 걸러진게 없으니 빼야함.
                break
        else:
            unusable_gems.add(item) # 쓸 수 없는걸 모아준다.

    while unusable_gems:
        current = unusable_gems.pop()
        while current in gems:
            gems.remove(current) # 이렇게 해서 다 제거함.
            # 문제점1 - 오답이(쓸 수 없는 gem) 여러개인경우 -> 해결
            # 문제점2 - 정답이(쓸 수 있는 gem) 여러개인경우 -> 해결

    gem_num = len(gems)
    approximate_target = 0
    for i in range(1 << gem_num):  # bit masking으로 조합 (경우의 수) 00000 ~ 11111
        combination = [0]          # 아무것도 못 뽑을거 대비.
        for j in range(gem_num):   # 2진수 자리수 대입 00001 00010 00100 01000 10000
            if i & (1 << j):
                combination.append(gems[j])
        temp_value = sum(combination)

        if temp_value == target_value:  # backtracking. gem개수 20개라서 혹시나 해서 넣음.
            approximate_target = temp_value
            break

        if approximate_target < temp_value <= target_value:
            approximate_target = temp_value

    print(f'#{case} {approximate_target}')







