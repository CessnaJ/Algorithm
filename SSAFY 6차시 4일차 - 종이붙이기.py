# 이곳에 코드와 주석을 작성합니다.
# memoization. 근데 이게 진짜 푼건지 모르겠네요. 야매입니다.
memo = [1, 3]

def paper_paste(n):
    global memo
    if len(memo) < n:
        if n%2: # 홀수면
            memo.append(memo[-1]*2 -1)
        else:   # 짝수면
            memo.append(memo[-1]*2 +1)
    return memo


def call_papaer_paste(n):
    for i in range(1, n+1):
        paper_paste(i)
    if n == 1:                      # 예외 조건
        return 1
    return memo[-1]

T = int(input())
for case in range(1, T+1):
    width = int(int(input())/10)
    print(f'#{case} {call_papaer_paste(width)}')