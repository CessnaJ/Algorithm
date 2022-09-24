V, E = map(int, input().split())  # Vertex, Edge 갯수

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 기본틀
cnt = 0

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_matrix[start][end] = 1
    # adj_matrix[end][start] = 1  # 양방향 그래프니까!!

stack = [1]  # 맨처음 시작점은 1번 포도알
visited = []  # 궤적 기록용

while stack:  # 스택이 빌때까지 돌아라!
    cnt += 1
    print(f'몇번째 사이클인지?{cnt}')
    current = stack.pop()  # 우선 스택에서 현재 위치 하나 뽑고
    print(current)
    if current not in visited:  # 방문하지 않은 곳이라면,
        visited.append(current)  # 방문했다고 체크해줌

    for destination in range(V+1):  # current 입장에서 어디로 갈 수 있는지 모조리 체크
        if adj_matrix[current][destination] and destination not in visited:  # 갈수있고 + 방문 안했으면!
            stack.append(destination)  # 다음 갈 곳으로 Stack에 저장

print('이동경로:', *visited)

# 이동경로: 1 3 7 6 5 2 4
#
# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7
# 1376524, 9