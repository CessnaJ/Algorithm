# 풀기 전 생각! python에서 string의 크기비교 연산은 사전순으로(한글자씩 비교) 이루어진다. string으로 이어서 크기를 비교하면 자연스럽게 풀릴것이다.
# 1,2,3 으로만 이루어진다는거! 경우의수 다 뽑아낸다음에, 정렬하면 됨.
number, order = map(int, input().split()) # 일단 1로 number개수만큼 돌리는게 최대개수다.


for digit in range(number):



def check_digit(n):
    if check_digit(n-1)[0] == number:
        return check_digit(n-1)[1]



# 이거 재귀로 풀면 될거같은데.. 맥스를 n개로 놓고, 123대입해서 다음 depth로 넘긴다음에 더해서 n 넘기면 return하고 아니면 다음 depth로 가는식으로. 그렇게 123 , 123에 연결된 123(그중에 n 넘으면 자르고, n이랑 똑같으면 append해서 list에 넣고.)
