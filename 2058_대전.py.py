N = int(input())

a = (N//1000)
b = (N//100)-(10*a)
c = (N//10)-(100*a + 10*b)
d = N - (1000*a + 100*b + 10*c)

print(a+b+c+d)