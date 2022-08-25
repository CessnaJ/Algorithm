def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    if n == 1:
        result = [[i] for i in arr]
        return result
    for i in range(len(arr)):
        elem = arr[i]
        p = permutation(arr[:i]+arr[i+1:], n-1)
        for rest in p:
            result.append([elem]+rest)
    return result
# 출처: https://naudhizb.tistory.com/1001 [Brise:티스토리]


T = int(input())

for case in range(1, T+1):
    card_set = set(range(1, 19))  # 타이핑 하기 귀찮아서 그냥 이렇게 받을게요. 18개 타이핑해서 set 안쓰고 어찌저찌하면 메모리 덜 쓰겠지만 귀찮습니다.
    counter_card_order = list(map(int, input().split()))  # 얘는 오더대로 낸다고 했네요.
    my_card_set = card_set - set(counter_card_order)
    my_card_list = list(my_card_set)  # 여기까지 귀찮은걸로 하고
    max_point = 171
    my_win = 0
    counter_win = 0
    my_permutation_list = []
    card_permutation_list = permutation(my_card_list, 9)

    for my_card_draw in card_permutation_list: # 9!개의 카드 순서가 다 들어있는..
        my_point = 0
        counter_point = 0
        for turn in range(9):
            if my_point >= 86: #점수 과반 났으면 더 볼 필요 없음.
                my_win += 1
                break
            elif counter_point >= 86:
                counter_win += 1
                break
            else:
                pass # 어떻게 해야 무승부가 되지? 카드도 똑같은거 못내고, 총점도 홀수인데?

            my_card_on_turn = my_card_draw[turn]
            counter_card_on_turn = counter_card_order[turn]
            if my_card_on_turn > counter_card_on_turn:
                my_point += (my_card_on_turn + counter_card_on_turn)
            else:
                counter_point += (my_card_on_turn + counter_card_on_turn)


    print(f'#{case} {my_win} {counter_win}')







    # for a in my_card_left:
    #     my_card_left[a]
    #     for b in :
    #         for c in :
    #             for d in :
    #                 for e in :
    #                     for f in :
    #                         for g in :
    #                             for h in:
    #                                 for i in:





#     for i in range(9): # 9번 승부~
#
#
#
#     print(f'#{case} ')
#
# print(sum(range(1,19)))




# if point >= 86:
#     my_win += 1
#     continue
# elif counter_point >= 86:
#     counter_win += 1