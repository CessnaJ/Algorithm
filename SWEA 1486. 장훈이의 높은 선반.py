# 풀기 전 생각!
# 이거 배낭문제인가? 배낭문제는 dp로.. 하.. 이거 다시 공부하자..
# bruteforce로 갈겨!

T = int(input())

for case in range(1, T+1):
    N, B = map(int, input().split()) # 사람수, 목표
    clerks = list(map(int, input().split()))  # B이상인 최소 탑 원소합.
    height_list = []
    for i in range(1<<N):
        subset = []
        height = 0
        for j in range(N):
            if i & (1<<j):
                subset.append(clerks[j])
        height = sum(subset)
        if height >= B:
            height_list.append(height)
    height_list.sort()
    print(f'#{case} {height_list[0] - B}')