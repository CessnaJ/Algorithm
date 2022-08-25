# 틀렸음. 다시 해야됨.

T = int(input()) # 테스트 케이스 T개

for _ in range(T): # 테스트 케이스 만큼 for loop
    N, L = map(int, input().split()) # 변수 받아야함. 문제 요구대로 N, L로 받음
    ingredient_list = [] # list속 list로 재료의 맛, 칼로리를 받을것임.(키 중복 우려로 dict 안씀)
    for i in range(N): # 재료가 N개니까 일단 다 넣어준다.
        ingredient_list.append(list(map(int, input().split())))
    max_taste = 0
    for a in range(N): # 완전탐색할건데, 돌리다가 칼로리 limit 넘으면 continue로 다음 try로 넘어감.
        if ingredient_list[a][1] > L:
            continue
        else:
            if max_taste < ingredient_list[a][0]:
                max_taste = ingredient_list[a][0]
            for b in range(a+1, N):
                if ingredient_list[a][1] + ingredient_list[b][1] > L:
                    continue
                else:
                    if max_taste < ingredient_list[a][0] + ingredient_list[b][0]:
                        max_taste = ingredient_list[a][0] + ingredient_list[b][0]
                    for c in range(b+1, N):
                        if ingredient_list[a][1] + ingredient_list[b][1] + ingredient_list[c][1] > L:
                            continue
                        else:
                            if max_taste < ingredient_list[a][0] + ingredient_list[b][0] + ingredient_list[c][0]:
                                max_taste = ingredient_list[a][0] + ingredient_list[b][0] + ingredient_list[c][0]
    print(f'#{_+1} {max_taste}')
    max_taste = 0
    #1 750