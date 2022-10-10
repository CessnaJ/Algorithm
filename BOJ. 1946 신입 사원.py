# T = int(input())
#
# for case in range(1, T+1):
#     N = int(input())
#     candidates = sorted([list(map(int, input().split())) for _ in range(N)])
#     # print(candidates)
#     interview_scores = list(zip(*candidates))[1]
#     # print(interview_scores)
#     cnt = 1
#     anchor = interview_scores[0]
#     for i in range(1, N):
#         if anchor > interview_scores[i]: # anchor에 비해서 새로 보는 친구가 등수가 높다(숫자가 작다 -> 우월하다/ 통과가 가능하다)
#             anchor = interview_scores[i] # 좋은 친구가 들어왔으니 기준이 더 빡세진다.
#             cnt += 1
#
#     print(f'{cnt}')

import sys
input = sys.stdin.readline
T = int(input())

for case in range(1, T+1):
    N = int(input())
    candidates = sorted([list(map(int, input().split())) for _ in range(N)])
    # print(candidates)
    interview_scores = list(zip(*candidates))[1]
    # print(interview_scores)
    cnt = 1
    anchor = interview_scores[0]
    for i in range(1, N):
        if anchor > interview_scores[i]: # anchor에 비해서 새로 보는 친구가 등수가 높다(숫자가 작다 -> 우월하다/ 통과가 가능하다)
            anchor = interview_scores[i] # 좋은 친구가 들어왔으니 기준이 더 빡세진다.
            cnt += 1

    print(f'{cnt}')