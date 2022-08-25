T = int(input())

for case in range(1, T+1):
    nodes, enroute = map(int, input().split())
    route_list = [[] for _ in range(nodes+1)]

    for i in range(1, enroute+1):
        depart, arrive = map(int, input().split())
        route_list[depart].append(arrive)

    start, end = map(int, input().split())

    stack = [start]
    visited = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)

        for destination in route_list[current]:
            if destination not in visited:
                stack.append(destination)
    if end not in visited:
        print(f'#{case} 0')
    else:
        print(f'#{case} 1')

