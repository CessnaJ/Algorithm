visited1 = []
visited2 = []


def dfs(anchor, visited_list):
    visited_list.append(anchor)
    if relation.get(anchor):
        for neighbor in relation[anchor]:
            if neighbor in visited_list:
                pass
            else:
                dfs(neighbor, visited_list)


T = int(input())
relation = {}
for _ in range(T-1):
    child, parent = input().split()
    if parent not in relation:
        relation[parent] = [child]
    else:
        relation[parent].append(child)
c, p = input().split()
# dfs(c, visited1)
dfs(p, visited2)

# if p in visited1 or c in visited2:
if c in visited2:
    print(1)
else:
    print(0)

