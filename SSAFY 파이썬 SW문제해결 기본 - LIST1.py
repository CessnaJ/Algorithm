# 쉽다. 빨리 풀자.
# list라는 container를 제대로 쓰자. index는 그냥 loop를 위한게 아니라 그 자체에 의미를 부여할 수 있다.


T = int(input()) # test case 개수



# idx가 숫자가 몇인지를 가리키고, list idx를 통해 접근한 integer가 해당 숫자(idx를 말함)가 몇개인지를 말해줌.
for case in range(1, T+1):
    count_list = [0] * 10
    N = int(input())  # 각 test case별로 N개의 카드
    card_num_input_by_str = input()
    idx_of_most_card = 0
    most_card_count = 0
    for i in card_num_input_by_str: # count_sort를 할거임.
        count_list[int(i)] = count_list[int(i)] + 1 # 넣어준다.

    for j in range(10):
        if count_list[j] >= count_list[idx_of_most_card]: # value가 높다? => most card다! >= 넣은 이유는 더 큰 숫자 받기위함.
            idx_of_most_card = j
    for k in card_num_input_by_str:
        int(k)

    print(f'#{case} {idx_of_most_card} {count_list[idx_of_most_card]}')
