# 길이 없을 수도 있다.
# 길 비용이 대칭적이지 않다.
# 일단 route를 만들면 그걸 1차적으로 anchor에 넣고
# anchor보다 도중에 커지면 prunning 해주자
# 다 돌았는데 anchor보다 작으면 anchor를 갱신해주자.

# 4
# 0 10 15 20
# 5  0  9 10
# 6 13  0 12
# 8  8  9  0

# from collections import deque

cities = int(input())

matrix = [list(map(int, input().split())) for _ in range(cities)]
visited = [False]*cities
# edges = deque()
edges = []
for start in range(cities):
    for end in range(cities):
        if matrix[start][end]:
            edges.append([matrix[start][end], start, end])
edges.sort()

min_cost = 999999999

while visited != [True]*cities:
    index = 0
    cost, start, end = edges[index]
    index += 1

    if not visited[end]:

        visited[end] = True


# visited =

# while visited != [True]*cities:
