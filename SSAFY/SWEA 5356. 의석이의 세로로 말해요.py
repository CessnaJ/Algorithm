# 의석이가 심심한가보다 밖에 나가서 공이나 차고 놀지.
T = int(input())
for case in range(1, T+1):
    print(f'#{case} ', end='')
    given_str_list = [input() for _ in range(5)] # 문제에서 5줄로 통일한다고해서 이렇게 받아옴. # 어차피 뭔가를 구하려면 순회를 돌려야되는데 그냥 메모리 좀 쓰고 쉽게 갈수있지않나?
    dummy_list = [['@'] * 5 for _ in range(15)]  # @로 된 list 15 * 5로 만들어서 바꿔 끼우고 @ 빼고 출력해버리면 되지않나? try except 생각을 했는데 그거보다 이게 컴퓨터 덜 쓸거같음.
#len max 돌리고 그만큼만 @ 끼워도 될거같긴 함.
# 어차피 갈아끼우는거 치환해서 갈아끼우면 됨.
    for i in range(5):
        for j, letter in enumerate(given_str_list[i]):
            dummy_list[j][i] = letter
    for row in dummy_list:
        for char in row:
            if char != '@':
                print(char, end='')
    print('',end='\n')