def gen(n):
    for digit in str(n):
        n += int(digit)
    return n

numbers = set(range(1, 10001))
number = 1
generated = set()

for i in range(1,10001):
    generated.add(gen(i))

answer = sorted(list(numbers - generated))
print(*answer, sep='\n')

# 솔직히 왜 1~10000을 for loop해야되는지 모르겠음.