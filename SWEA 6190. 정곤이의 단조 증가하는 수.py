# list 받아서 단조증가하는 수 모아서 새로 list up(map쓰면서 이제서야 int형으로 변환하면서)하고, 그중에 brute force 돌리면서 최대숫자 2개 뱉을거임.
T = int(input())
for case in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    multiple_list = []
    #이제 최대 곱 되는 2 숫자 찾을것.
    maximum_multiple = 0
    pass_list = []
    for i in range(N):
        for j in range(i+1, N):
            multiple = num_list[i] * num_list[j]
            multiple_list.append(multiple)
    print(multiple_list)


    for element in multiple_list:  # 받아온거 한개씩 검증
        if len(str(element)) == 1:  # 1자리수면 어차피 걍 넣을거임.
            pass_list.append(element)
        else:
            # check_increasing = element[::-1] # 반대로 돌려서 검증 시작.
            for idx in range(len(str(element)) - 1):
                if not str(element)[idx] <= str(element)[idx + 1]:  # 1번이라도 안맞으면 바로 깽판
                    break
            else:  # 완주시 바뀌기 전 str 넣음.
                pass_list.append(element)
    if not pass_list:
        print(f'#{case} {-1}')
    else:
        print(f'#{case} {max(pass_list)}')


