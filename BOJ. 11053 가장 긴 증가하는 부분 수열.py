N = int(input())

arr = list(map(int, input().split()))
subproblem = [1] * (N) # idx와 동기화 위해 +1

# Dynamic programming
# subproblem으로 나눠서 수열이 몇개가 되든
# 그 수열번호까지 최대가 되는 증가하는 수열의 element 개수를 count 해줄 수 있어야한다.
# 해당 element번호에 넣어줄 수 있는 빈 배열을 만들어서 거기에 몇개인지 채워주면 된다.
# 특정 element의 차례가 되면, 그 element보다 '작은' 배열을 역순으로 탐색해서 찾게된다면
# (가장먼저 만난게 가장 큰 숫자일테니) 그 배열 idx에 넣어진 숫자에 1을 더해주는식으로 답안지를 채워나간다.
# and 뒤에 온 조건은, 내가 앞에거를 찾아서 한번 더해본거랑 비교해서, 너를 골라서 1 더한게 더 나은지 보자는 뜻임.

for anchor in range(len(arr)):
    for comparison in range(anchor, -1, -1):
        if arr[anchor] > arr[comparison] and subproblem[comparison] >= subproblem[anchor]:
            subproblem[anchor] = subproblem[comparison] + 1

print(max(subproblem))

