# 반복 하는게 더러워서 calling 함수 하나 더 만들어서 호출시켜버림. 그렇다고 기존 함수에 그냥 콜링 기능까지 넣는건 별로인거같아서?

def pascal_row_using_memoization(n):
    global memo
    if n >= 2 and len(memo) < n:
        new_row = [1]
        for i in range(len(memo[-1])-1):
            new_row.append(memo[-1][i] + memo[-1][i+1])
        new_row.append(1)
        memo.append(new_row)
    return memo[n-1]
memo = [[1], [1, 1]]

def call_pascal(n):
    for i in range(1,n+1):
        print(*pascal_row_using_memoization(i))

call_pascal(3)