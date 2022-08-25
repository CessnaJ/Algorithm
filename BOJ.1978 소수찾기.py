N = int(input())

num_list = map(int, input().split())
how_many_prime_num = 0
for i in num_list:
    if i == 1:
        continue
    elif i ==2:
        how_many_prime_num += 1
        continue
    else:
        for j in range(2,i):
            if i % j != 0:
                pass
            else:
                break
        else:
            how_many_prime_num += 1

print(how_many_prime_num)