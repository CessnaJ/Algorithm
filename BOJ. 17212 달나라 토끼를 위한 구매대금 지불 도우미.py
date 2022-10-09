# # DP로 풀면 될거같다. 근데~ 여기서 최소공배수 개념이 나오면 더 효율적이지 않을까? 어차피 단위수가 옃개 없다~
# target = int(input())
# bag = [1, 2, 5, 7]
# subproblem = [0]+ [99999999]*(target) # 0번 인덱스는 버린다.
#
#
# for amid in range(1, target+1):
#     for coin in bag:
#         if amid - coin >= 0 and subproblem[amid] > subproblem[amid-coin]+1:
#             subproblem[amid] = subproblem[amid-coin]+1
# print(subproblem[-1])
# print(subproblem, sep='\n')



# DP로 풀면 될거같다. 근데~ 여기서 최소공배수 개념이 나오면 더 효율적이지 않을까? 어차피 단위수가 옃개 없다~
target = int(input())
bag = [7, 5, 2, 1]
subproblem = [0]+ [999999]*(100000) # 0번 인덱스는 버린다.


for amid in range(1, target+1):
    for coin in bag:
        if amid - coin >= 0 and subproblem[amid] > subproblem[amid-coin]+1:
            subproblem[amid] = subproblem[amid-coin]+1
            break
print(subproblem[target])

