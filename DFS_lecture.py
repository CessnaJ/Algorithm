V, E = map(int, input().split())

adj_matrix = [[0] * (V + 1) for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

print(adj_matrix)

stack = [1]
visited = []

# pop(0)하면 queue 쓰겠다는 것, pop()은 LIFO로 쓰겠다는것. stack.


while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in range(V + 1):
        if adj_matrix[current][destination] and destination not in visited:
            stack.append(destination)

    print(stack)
    print(visited)

