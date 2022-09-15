T = int(input())
value = 0


def inorder(idx):
    global value

    if idx <= N:
        inorder(idx * 2)

        idxValueTree[value+1][0] = value
        value += 1

        inorder(idx*2 + 1)


for case in range(1, T+1): # 이거 중위탐색 해나가면서 더 못가면 global변수 이용해서 채워나가면 될거같다? 아니면 층을 파악해서 완전이진트리 만들고 몇개 삭제를 할까?
    N = int(input())
    idxValueTree = [[0, i] for i in range(N+1)] # 0은 버리니까. 채워나갈값인 앞 element를 0으로 둠. i는 idx를 이야기함.
    inorder(1)
    tree_sorted_by_value = sorted(idxValueTree)

    print(f'#{case} {tree_sorted_by_value[1][1]} {tree_sorted_by_value[N//2][1]}')