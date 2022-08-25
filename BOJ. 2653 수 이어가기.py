# making recursive function using memoization
# 풀기 전 생각! - 간단한 문제. 1부터 N까지 싹 돌려주면서 최대값 찾으면 됨. dp로 실행시간 줄여주는게 가능할거같긴함.

first_num = int(input())                             # 받고 싶은 첫 숫자
max_length = 0                                       # 출력하고 싶은거 1
max_list = []                                        # 출력하고 싶은거 2
for i in range(1, first_num+1):                      # 1부터 brute force
    length = 0
    dsc_list = [first_num]                           # refresh
    dsc_list.append(i)                               # 일단 대상숫자 넣어야 반복 가능.
    while dsc_list[-1] >= 0:                         # 마지막 숫자 음수 나올때까지 반복
        dsc_list.append(dsc_list[-2] - dsc_list[-1]) # 원하는 계산 이어줌
    length = len(dsc_list)                           # 계산 끝나면 길이
    if length > max_length:                          # 가장 긴걸로 갱신 해줌
        max_length = length
        max_list = dsc_list

print(max_length - 1)                                # 음수되는것까지 포함을 시켰기에 마지막거는 제외해줌.
print(*max_list[:-1])                                # 재귀로 풀고 싶은데 시간 투자를 못하겠음 ㅜ.
