T = int(input())

for case in range(1, T+1):
    n = int(input())
    i = n**(1/3)
    print(i)
    print(type(i))
    if type(i) == type(1):
        print(f'#{case} {i}')
    else:
        print(f'#{case} {-1}')

# 이거 소수점 무한소수나오는거 처리만해주면 됨. 영록님이랑 다른방법 없을까 생각하다가 그냥 이렇게 냅둠.