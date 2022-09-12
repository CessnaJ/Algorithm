N, K = map(int, input().split())

sieve = list(range(2, N+1))
removed_list = []
count = 0
while sieve:
    P = sieve[0]
    for num in sieve:
        if not num % P:
            count += 1
            sieve.remove(num)
            if count == K:
                print(num)
