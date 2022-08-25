T = int(input())
# 전형적인 bfs 알고리즘이다.


def bfs(graph, start_node, end_node): # 이 함수는 완성된 인접list, start
    visited_list = [start_node]       # visited list에 방문한 모든 지점을 넣어서 재방문 안하게 한다.(loop발생방지)
    count = 0
    q = [(count, start_node)]                  # q에 앞으로 방문할 애들을 순차적으로 넣을것이다.
                                      # 깊이별로 카운트를 올릴건데 이거 좀 고민이 된다.
    while q:                          # q가 아예 비었다는게, 밀려있는게 전혀없고, 앞으로 넣어줄것도 없다는 뜻.
        m = q.pop(0)                  # FIFO모양을 만들기 위해 맨 뒤의 element에 삽입, 그리고 맨 앞 element를 pop해줄것이다.
                                      # 그리고 pop 특성으로 나오게 된걸 변수로 저장한다.
        for neighbour in graph[m[1]]:    # 큐에서 순서가 된 노드를 중심으로 갈 수 있는곳들을 탐색하는식이다.
            if neighbour not in visited_list:   # 가본적 없는 이웃들을
                visited_list.append(neighbour)  # 일단 visited에 넣으면서
                q.append((m[0]+ 1, neighbour))             # 앞으로 갈 친구들 목록에 넣어서 줄세운다. 이러면 순차적으로 방문하게 된다.

        if end_node in visited_list:
            return m[0]+1

    if end_node not in visited_list:
        return 0

for case in range(1, T+1):
    V, E = map(int, input().split())
    adjacent_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        start, end = map(int, input().split())
        adjacent_list[start].append(end)
        adjacent_list[end].append(start)

    dep_node, arr_node =  map(int, input().split())
    # print(adjacent_list)
    # q_list = [dep_node]
    # visited = [dep_node]

    print(f'#{case} {bfs(adjacent_list, dep_node, arr_node)}')