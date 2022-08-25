# 이것도 한 10분컷 가능하겠지.. 3시 8분 시작~
# 풀기 전 생각!
# 동 서 남 북 -> [1, 2, 3, 4] x +- 그리고 y - + 이렇게 주고 있음.
# input 다 받아서, 어차피 다 합쳐질거기 때문에
# 결국 작은 사각형, 큰 사각형 두개로 구성되는거라서, 사각형 성질을 이용해보자.
# 가장 큰 변의 길이가 가로 길이일것이고(width), 그게 되는 두 변의 합이 가로 쪼개기가 될것이다.(a +b로 보자) 찾는건 brute force로 찾자~
# 받은 list에서 a, b, width를 빼면, 그 뒤에 남는건 뻔하지. (length, 그리고 나머지것들 c + d 라고 하자.)

#3시 14분. 자세히 보니까 방향이 동서남북으로 이어지면 그 선분들은 짤라먹는 선분이 아니다. => 이렇게 접근하면 답은 나오겠지만 더 복잡해진다. 심플하게 패턴을 찾자.

# 이거는 idx에 loop가 돌게해서, end tip에 걸렸을때는 0으로 다시 갈 수 있도록 조치를 취해야한다.
# if statement로 가능함.

density = int(input())
direction_distance_in_list = [list(map(int, input().split())) for _ in range(6)]
small_square = []
large_square = []
small_square_idx = []
for i in range(6): # idx -1 되는건 괜찮으니까 놔두고 6되는것만 막아주자.
    if i == 5: # a,b는 i의 앞,뒤 idx를 말하는것.
        a, b = 4, 0
    else:
        a, b = i-1, i+1

    if direction_distance_in_list[a][0] == direction_distance_in_list[b][0]: # 패턴발견. idx의 앞뒤 direction이 겹친다면~
        small_square.append(direction_distance_in_list[i][1]) # 해당 길이를 넣어준다.
        large_square.append(direction_distance_in_list[a][1] + direction_distance_in_list[b][1]) # 근데 앞뒤의 방향이 같다는게, 두 변을 합쳤을때 큰 변이 된다는 뜻이다. 문제의 패턴과 특성을 이용한다.
print((large_square[0] * large_square[1] - small_square[0]* small_square[1]) * density) # 이렇게 풀다니.. 어이가 없음.. 근데 간단한거를 25분 걸렸습니다.



        # small_square_idx.append(i) # 그리고 그 변이 있는 idx를 넣어서 계산 쉽게. # idx 두개를 더해서 같은 방향이 아니면 그게 긴 변이라는 뜻임.
