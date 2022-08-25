num = 456789
c = [0]* 12 #왜 12개인가? -> triple조사하는 idx랑 run 조사하는 idx의 끝을 구분짓지않고 통일시켜서 while문으로 쉽게 비교하기 위해.
for i in range(6): #1~2칸 더 붙히는거는 메모리에 거의 영향이 없으니, 이걸 통해서 계산 단계를 줄이는게 더 이득임.
    c[num%10] += 1
    num //= 10

i = 0
tri = run = 0

while i < 10:
    if c[i] > 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1
if run + tri ==2:
    print('Baby gin')
else:
    print('Lose')