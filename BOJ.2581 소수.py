M = int(input())
N = int(input())

num_list = list(range(M,N+1))
prime_num_list = []
if M == 1 and N == 2:
    print(-1)
elif M == 1:
    M = 2
    num_list = list(range(M, N + 1))
    prime_num_list = []
    for i in num_list:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            prime_num_list.append(i)


    if len(prime_num_list) == 0:
        print(-1)
    else:
        print(sum(prime_num_list), min(prime_num_list), sep='\n')

else:
    for i in num_list:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            prime_num_list.append(i)


    if len(prime_num_list) == 0:
        print(-1)
    else:
        print(sum(prime_num_list), min(prime_num_list), sep='\n')


'''
좆밥문제 틀린거 열받아서 걍 복붙으로 갈겼는데 이러지말자..
'''