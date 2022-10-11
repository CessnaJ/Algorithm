T = int(input())
import copy
from itertools import combinations

# def strength_test(matrix, d, w, s):
#     anchor = matrix[0][0]
#     cnt = 0
#     failed = False
#     for i in range(w):
#         for j in range(d):
#             if anchor == matrix[i][j]:
#                 cnt += 1
#                 if cnt == s:
#                     break
#             else:
#                 anchor = matrix[i][j]
#                 cnt = 0
#         else:
#             failed = True
#         if failed:
#             return False
#     return True
#
#
#
# for case in range(1, T+1):
#     depth, width, sequence = map(int, input().split())
#     matrix_before = [input().split() for _ in range(depth)]
#
#     changes = 0
#     if strength_test(matrix_before, depth, width, sequence):
#         print(f'#{case} 0')
#
#     else:
#         changes += 1
#         combinations()
#         combi = list(combinations(range(changes)))
#         for i in
#
#
#     print(f'#{case}')


print(combinations([0,1]))



