T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split()) # 정수의 개수 N과 구간의 개수 M
    given_list = list(map(int, input().split()))
    min_sum = 0
    max_sum = 0

    for i in range(0, N-M+1): # index의 limit을 어떻게 줄것이냐? N개의 숫자카드중에서 M개씩 묶으니까 저렇게.
        temp_sum = 0
        for j in given_list[i:i+M]:
            temp_sum += j
        if max_sum == 0:
            max_sum = temp_sum
        elif temp_sum > max_sum:
            max_sum = temp_sum
        else:
            pass

        if min_sum == 0:
            min_sum = temp_sum
        elif temp_sum < min_sum:
            min_sum = temp_sum
        else:
            pass
    print(f'#{case} {max_sum - min_sum}')