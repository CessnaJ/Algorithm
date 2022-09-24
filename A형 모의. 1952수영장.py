from collections import defaultdict

# T = int(input())

# for case in range(1, T+1):
#     daily, monthly, quarterly, yearly = map(int, input().split())
#     plan = list(map(int, input().split()))
#     cost = [0]*12
#     quarterly1_candidate = []
#     quarterly2_candidate = []
#     for i in plan:
#         if plan[i] * daily >= monthly:
#             cost[i] = monthly
#         else:
#             cost[i] = plan[i] * daily
#     for j in range(12):
#         temp = quarterly
#         quarterly1_candidate.append(sum(cost[:j]) + sum(cost[j+3:]) + temp)
#
#     for k in range(7):
#         if sum(cost[k:k+3]) < quarterly:
#             continue
#         for l in range(k+3,10):
#             temp = sum([2*quarterly, cost[k], cost[k+1], cost[k+2], cost[l], cost[l+1], cost[l+2]])
#             quarterly2_candidate.append(temp)
#     answer = [yearly, sum(cost)]
#     if quarterly1_candidate:
#         answer.append(min(quarterly1_candidate))
#     if quarterly2_candidate:
#         answer.append(min(quarterly2_candidate))
#     print(f'#{case} {min(answer)}')


# 스터디에서 비슷하게 진행한 배낭 스타일 dp 문제.
T = int(input())                   # test case 받아온다.

for case in range(1, T+1):
    daily, monthly, quarterly, yearly = map(int, input().split()) # 가격표 변수 받아옴
    plan = [0] + list(map(int, input().split()))                  # 월에 몇일 쓸지? 밑에 month-1이랑 idx에러 안나게 이어지려고 13으로 해놨음.
    cost = [0] * 13                                               # 누적으로 만들어나갈 누적 월 지불액

    for month in range(1, 13):
        cost[month] = min(daily * plan[month], monthly) + cost[month-1] # 일단 월은 간단하게 둘중 작은걸로 대체.

        if month >= 3:         # 3부터 분기 비교 시작. 123월까지의 누적 month합이 분기가격보다 비싸면 싼걸로 대체.
            cost[month] = min(cost[month], quarterly+cost[month-3]) # 딱딱 안떨어져도 어차피 누적합이기 떄문에 3달전 누적합이랑 비교해서 더 싸면 대체되는 식임.
    affordable = min(cost[12], yearly) # 마지막은 연간회원권이랑 비교.

    print(f'#{case} {affordable}')