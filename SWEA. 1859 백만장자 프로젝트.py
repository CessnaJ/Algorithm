T = int(input())

for case in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    # 역방향 index부터 해서 while시작.
    # 첫idx max걸고, 한칸씩 나가면서 max보다 작으면 그거 합산.
    # 더 크면 새 max로 리셋하고 다시 시작.
    # 첫 idx까지와서 다 더해줬으면 while문 터뜨리고 print


    print(f'{case}')