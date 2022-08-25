#N=2a x 3b x 5c x 7d x 11e

# N이 주어질 때 a, b, c, d, e 를 출력하라.

T = int(input())

for case in range(1, T+1):
    target_num = int(input())
    count_a2 =0
    count_b3 = 0
    count_c5 = 0
    count_d7 = 0
    count_e11 = 0
    while not target_num%2:
        target_num //= 2
        count_a2 +=1
    while not target_num%3:
        target_num //= 3
        count_b3 += 1

    while not target_num%5:
        target_num //= 5
        count_c5 += 1

    while not target_num%7:
        target_num //= 7
        count_d7 += 1

    while not target_num%11:
        target_num //= 11
        count_e11 += 1

    print(f'#{case} {count_a2} {count_b3} {count_c5} {count_d7} {count_e11}')