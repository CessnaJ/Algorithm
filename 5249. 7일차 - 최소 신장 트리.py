def make_set(x):
    top_ancestor_of_idx[x] = x
    # 각 node의 초기값은 자기 자신이 대표라는 뜻



def find_top_ancestor(child):
    if top_ancestor_of_idx[child] != child:
        top_ancestor_of_idx[child] = find_top_ancestor(top_ancestor_of_idx[child])

    return top_ancestor_of_idx[child]  # 왜 if 밖에 있어야할까?



def union(merger, mergee):
    top_ancestor_of_idx[find_top_ancestor(mergee)] = find_top_ancestor(merger)



T = int(input())

for case in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])
    top_ancestor_of_idx = [0]*(V+1)

    for i in range(V+1):
        make_set(i)
    # print(top_ancestor_of_idx)
    answer = 0
    count = 0

    for merger, mergee, weight in edges:
        # print(find_top_ancestor(merger))
        # print(find_top_ancestor(mergee))
        if find_top_ancestor(merger) != find_top_ancestor(mergee):
            union(merger, mergee)
            answer += weight
            # print(weight)
            count += 1
            if count == V:
                break
    # print(count)
    print(f'#{case} {answer}')