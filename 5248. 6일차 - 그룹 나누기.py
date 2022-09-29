def make_set(x):
    top_ancestor_of_idx[x] = x
    # 각 node의 초기값은 자기 자신이 대표라는 뜻

def find_top_ancestor(child):
    # child라고 하는 해당 list의 idx element에 접근하도록 parameter를 넣었으니 list 자체는 못바꾸더라도 그 안에 있는 element는 바꿀 수 있다?
    if top_ancestor_of_idx[child] != child:
        top_ancestor_of_idx[child] = find_top_ancestor(top_ancestor_of_idx[child])

    return top_ancestor_of_idx[child]  # 왜 if 밖에 있어야할까?


def union(merger, mergee):
    top_ancestor_of_idx[find_top_ancestor(mergee)] = find_top_ancestor(merger)


T = int(input())

for case in range(1, T+1):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))

    top_ancestor_of_idx = [0] * (V + 1) # 틀만들고
    for j in range(V+1): # 기본형으로 틀 채워넣기
        make_set(j)

    for i in range(E): # 순서 바로잡기. 이을때 낮은 숫자가 조상되는걸로 규칙 정했음.
        start, end = min(edges[i*2], edges[i*2 + 1]), max(edges[i*2], edges[i*2 + 1])
        union(start, end)

    answer = len(set(top_ancestor_of_idx[1:])) # 몇개의 그룹인가? idx0은 버리기로 했으니 이렇게.


    print(top_ancestor_of_idx)
    print(f'#{case} {answer}')


# 2 3
# 4 5
# 4 6
# 7 4
# 1 2-3 4-5-6-7