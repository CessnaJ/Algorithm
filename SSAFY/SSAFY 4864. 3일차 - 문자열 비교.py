T = int(input())

for case in range(1, T+1):
    piece = input()
    full_str = input()
    if piece in full_str:
        print(f'#{case} {1}')
    else:
        print(f'#{case} {0}')