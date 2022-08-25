# 모멘텀 계산해주는 (한번 작아지기 시작하면 착은것만 탐색. 한번 커지기 시작하면 큰것만 탐색) 근데 수열의 첫 2~3글자가 같으면?

# 이러면 어떨까? couunt의 기본을 1로 하고, consecutive_increase, consecutive_decrease 카운트를 새김(처음에 같은숫자 10개나오면 그걸 고려해주기 위함). 만약에 같으면 시작되었으면 다음꺼. 이전에 비해서 consecutive증가 안되면 다시 1로 리셋하기.
N = int(input())
given_num_list = list(map(int, input().split()))
consecutive_decrease = 1
consecutive_increase = 1
max_count = 0
for i in range(1, N): # 왼쪽부터 길이 탐색.
    temp_increase = consecutive_increase + 0
    temp_decrease = consecutive_decrease + 0
    if given_num_list[i] == given_num_list[i-1]:
        consecutive_increase += 1
        consecutive_decrease += 1
    elif given_num_list[i] > given_num_list[i-1]:
        consecutive_increase += 1
    elif given_num_list[i] < given_num_list[i-1]:
        consecutive_decrease += 1
    else:
        pass
    if temp_decrease == consecutive_decrease: # 직전 턴에 비해서 이어지지 않았다면 리셋.
        if consecutive_decrease > max_count:  # 리셋 전에 수치 저장할지 안할지.
            max_count = consecutive_decrease + 0
        consecutive_decrease = 1
    if temp_increase == consecutive_increase:
        if consecutive_increase > max_count:
            max_count = consecutive_increase + 0
        consecutive_increase = 1              # 아 max 갱신을 순열 마지막까지 완주 했을때도 해야지~
else:
    if consecutive_decrease > max_count:  # 순열이 마지막까지 안끊길수 있음. 위에 있는 조건만 붙으면 끊겼을때만 갱신을 하게 됨.
        max_count = consecutive_decrease + 0
    if consecutive_increase > max_count:
        max_count = consecutive_increase + 0

print(max_count)