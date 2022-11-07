# N(1 ≤ N ≤ 200,000), T(N ≤ T ≤ 100,000,000)
# N이상인 T일 동안 재배한다.
# 다음 N개의 줄에 걸쳐서 i+1번째 줄에 당근 i의 wi와 pi가 공백으로 구분되어 주어진다.
# T일 동안 토끼가 먹을 수 있는 당근의 맛의 합의 최댓값
# pi는 항상 wi이상의 값
# 처음에는 wi의 맛
# pi만큼 맛을 증가시켜주는 영양제가 당근 종류별로 T개씩 준비
# 토끼가 T일 동안 먹을 수 있는 당근의 맛의 합의 최댓값을 출력한다 왜? - 안먹을 수도 있다는거는 영양제의 증가치가 새로 심는거보다 더 좋다는 것.
# 토끼는 초기화를 시킴 0으로.
# 오리는 비어있으면 일단 그거 심고, 있으면 그중에 가장

# 생각.
# 가장 맛있는걸 최대한 아껴먹는게 이득이다. 마지막날에 최대값이 되는걸 마지막에 먹고
# 그 전날에 최대값이 되는 것을 그 전날에 먹고
# 반복을 하게 될거다.
# 다 냅뒀다고 쳤을때, T일 뒤 값을 정렬시키고. 걔를 먹고 pop
# 그 전날값으로 다 영양제 밸류만큼 빼기. pop해서 더하기
# 어쩔수 없이 대소비교를 해야된다 왜? - 기본값이 차이가 엄청나는 경우가 있기 때문. 중간에 역전을 하게 되는 경우가 발생
# from sys import stdin
#
# carrots, days = map(int, stdin.readline().split())
# carrot_list = [list(map(int, stdin.readline().split())) for _ in range(carrots)]  # [[default, increment]..]
# taste_sum = 0
#
# carrot_list.sort(key=lambda x: x[1])
#
# for default, increment in carrot_list:

from sys import stdin

carrots, days = map(int, stdin.readline().split())
carrot_list = list(zip(*[list(map(int, stdin.readline().split())) for _ in range(carrots)]))  # [[default, increment]..]
taste_sum = sum(carrot_list[0]) # 일단 당근 다먹을거니까

increment_list = sorted(list(carrot_list[1]))  # asc sort

for i in range(carrots):
    taste_sum += increment_list[i] * (days-carrots + i ) # 가장 맛없는거부터 먹을거야 (마지막에 가장 맛있는 영양제 농축만 먹게)
print(taste_sum)
#
# for i in range(carrots):
#     carrot_list[i].append(carrot_list[i][0] + carrot_list[i][1]*(days-1))  # [초기값, 증가분, 마지막날의 맛]
#
# carrot_list.sort(key=lambda x: x[2])
# taste_sum += carrot_list.pop()[2]
#
# if carrots > 1:
#     for j in range(carrots-1):
#         for k in range(len(carrot_list)):
#             carrot_list[k][2] -= carrot_list[k][1]
#         carrot_list.sort(key=lambda x: x[2])
#         taste_sum += carrot_list.pop()[2]
#
# print(taste_sum)
# 이거 힙큐 쓰면 좋을거같긴 함.
# for index in range(carrots):
#     carrot_taste = [carrot_list[index][0] + carrot_list[index]]

# 계속 계산할 필요가 있을까? 그냥 빼버릴바에는 가장 맛있는 상태의 N번을 먹게 될테니까 그것만 계산해서 가져가면 되지않나?
#
# n, t = map(int, sys.stdin.readline().split())
# carrots = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]  # w(현재), p(증가)
# carrots.sort(key=lambda x: x[1])
#
# result = 0
# feeded_days = t - n
# for w, p in carrots:
#     result += (w + p * feeded_days)
#     feeded_days += 1
#
# print(result)
