# 문제 풀기 전. 어떻게 풀것인가?
# 10 번 try. 2칸 옆으로 뚫려있으면 조망권 확보된 집이라고 보는거임. 7 8 10 5 5 이런식이면 옆 2개씩 봐서 가장 크면서,
# 가장 difference 작은 숫자가 들어가게 됨. 그리고, 만약에 가장 큰 뭔가가 나왔다고 치자 그러면 굳이 그 뒤 2개를 셀 필요가 없음.
# list로 일단 변수 N번째 숫자 봤을때 N-2 N-1 N+1 N+2 비교해서 min으로 차이나는거 (list slicing 통해서 해결하면 될듯)

#  솔루션 코드를 작성합니다.
for solution in range(10):       # 10회 try
    num_of_house = 0             # 변수 refresh
    min_height_difference = 256  # 변수 refresh. 층의 max가 255라서 다른 값에 영향을 안주면서 적당한게 256이라고 봤습니다.
    skip = 0                     # 한번 조망권이 있는 건물이 나오면 그 다음 2회 cycle은 당연히 조망권이 없게됩니다. 2회분 trial을 skip합니다.
    view_checking = [-2, -1, 1, 2] # index에 더해서 N번째 건물과 양옆 2개씩의 건물 높이를 비교하기 위함입니다.
    N = int(input())             # input 받아줍니다.
    buildings_height_list = list(map(int, input().split())) # input 받아줍니다 list로 받습니다.
    for i in range(N)[2:-2]:     # 첫 2, 마지막 2 빌딩은 고려사항이 아닙니다.
        if min_height_difference != 256: # 초기 값인 256이 아니고 조망권이 나왔다고 하면 2번 스킵하기 위한 코드입니다.
            skip = 2
            min_height_difference = 256
        if skip != 0:
            skip -= 1
            continue               # 스킵하는 도중에 밑에 코드는 볼것도 없죠.

        height_difference_list =[] # 비교해주기 위한 빈 리스트
        for j in view_checking:    # append 안쓰기 위해 이렇게 했습니다. []를 씌워줘야한다는걸 처음 알았습니다.
            height_difference_list += [buildings_height_list[i] - buildings_height_list[i + j]]

        for k in height_difference_list: # 하나씩 비교해보면서 생각한 핵심 아이디어는 다음과 같습니다.
            if k < 0:                    # 일단 리스트 비교 중 높이차에서 한번이라도 양수가 안나오면 최고 높이가 아니라는 뜻이므로,
                min_height_difference = 256 # 변수 refresh해주고
                break                       # 다음 사이클로 갑니다.
            elif min_height_difference > k:
                min_height_difference = k
        else:                                # break가 안나온다는거는 테스트 돌려서 값이 모두 양수이고,
            if min_height_difference != 256: # min_height_difference에 최소높이차가 들어갔다는 뜻이므로 집 수에 더해줍니다.
                num_of_house += min_height_difference

    print(f'#{solution + 1} {num_of_house}') # loop 다 돌고 결과값 출력.






# 10 번 try. 2칸 옆으로 뚫려있으면 조망권 확보된 집이라고 보는거임. 7 8 10 5 5 이런식이면 옆 2개씩 봐서 가장 크면서,
# 가장 difference 작은 숫자가 들어가게 됨. 그리고, 만약에 가장 큰 뭔가가 나왔다고 치자 그러면 굳이 그 뒤 2개를 셀 필요가 없음.
# list로 일단 변수 N번째 숫자 봤을때 N-2 N-1 N+1 N+2 비교해서 max차이나는거 (list slicing 통해서 해결하면 될듯)

# num_of_house = 0
# min_height_difference = 256
# skip = 0
# view_checking = [-2, -1, 1, 2]
# for _ in range(10):
#     N = int(input())
#     buildings_height_list = list(map(int, input().split()))
#     for i in range(N)[2:-2]:
#
#         if min_height_difference != 256:
#             skip = 2
#             min_height_difference = 256
#         if skip != 0:
#             skip -= 1
#             continue
#
#         height_difference_list =[]
#         for j in view_checking:
#             height_difference_list += [buildings_height_list[i] - buildings_height_list[i + j]]
#
#         for k in height_difference_list:
#             if k < 0:
#                 min_height_difference = 256
#                 break
#             elif min_height_difference > k:
#                 min_height_difference = k
#         else:
#             if min_height_difference != 256:
#                 num_of_house += min_height_difference
#
#     print(num_of_house)





