# 어떻게 풀 수 있을까?
# 1.N보다 크거나 같다.
# 2. 소수다 (에라토스테네스의 체)
# 3. 팰린드롬이다
# 3가지 조건을 다 만족해야한다.
# 테스트케이스가 독립적으로 발동하면 반복실행으로 그냥 하면 되는데,
# 이거 계산을 너무 많이하게 될거같다. 메모이제이션으로 할 수 있을까?
# 백준은 테스트케이스마다 계산을 새로 하지 않나?

def palindrome_test(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        return True


N = int(input())

# N보다 크거나 같다 니까..  N~100001로 for loop 진행해주면서
# 2~N//2까지 에라토스테네스의 체로 걸러주자. range(3,N//2,2)

possible_nums = list(range((N//2)*2 + 1, 1000000, 2)) # 짝수는 애초에 고려안해. N이 홀수인지 짝수인지 모르니까 이렇게.

possible_tf = [False, True]*500000 # 0은 제끼고, 홀수는 True, 짝수는 False. True가 소수라는걸 뜻하는 idx가 숫자 자체인 list를 만들것이다.

# possible_tf[-1] = False # 실험해봤는데 얕은복사로 문제 안생김.


for i in range(3, N//2, 2):
    k = 1
    sieve_num = i * k
    while sieve_num < 1000000:
        possible_tf[sieve_num] = False
        k += 1

for j in range(N, len(possible_tf)):
    if possible_tf[j] and palindrome_test(j):
        print(j)
        break