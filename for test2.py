def stack_dfs(node):
    stack = [node]  # 기준으로 할 node를 list에 넣어줌.
    visited = []  # loop 방지. visited list 만듬.

    while stack:  # stack이 비었다는건, 다 visited 처리되어서 더 이상 갈 곳이 없다는 뜻임.
        current = stack.pop()  # 일단 stack에서 하나 뽑아서 변수처리 (방문 후보들 하나씩 볼거.)
        if current not in visited:  # 아직 방문 안했다면
            visited.append(current)  # current 처리 (방문했다는 도장 찍기)
            # <custom하려면 여기에 뭔가를 넣는게 좋다.>
            if graph[current]:  # 그 current가 갈 수 있는 새 목적지가 있다면,
                for destination in graph[current]:
                    # 목적지들 순회 돌면서..(다음 while에서 방문가능한지)
                    stack.append(destination)
            # 가능한지는 다음 while문에서 current 뽑아보면서 볼거니까, 일단 넣음.


def matrix_stack_dfs(node):
    stack = [node]
    visited = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)

        for destination in range(V + 1):  # 작은번호 먼저 순회하는 dfs 만들려면 range(V, 0, -1)
            if matrix[current][destination] and destination not in visited:
                stack.append(destination)
