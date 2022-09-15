def preorder(n, count):

    if arr2[n]:
        preorder(arr1[n], count+1)
        preorder(arr2[n], count+1)
    elif arr1[n]:
        preorder(arr1[n], count+1)
    return count+1


T = int(input())
for case in range(1, T+1):
    count = 0
    E, N = map(int, input().split()) # 간선의 개수 E,// N을 root로 하는 subtree에 속한 node 개수 찾는거니까..
    arr1 = [0]*1002
    arr2 = [0]*1002
    #1001 이라고 해서 틀림. 1002.
    input_list = list(map(int, input().split()))

    for j in range(E): # arr1, arr2 나눠서 수납. line개수만큼 수납됨.
        if not arr1[input_list[2*j]]:
            arr1[input_list[2*j]] = input_list[2*j + 1]
        else:
            arr2[input_list[2*j]] = input_list[2*j + 1]
    print(f'#{case} {preorder(N, count)}')

    # for j in range(0, len(input_list), 2): # arr1, arr2 나눠서 수납.
    #     if not arr1[j]:
    #         arr1[input_list[j]] = input_list[j + 1]
    #     else:
    #         arr2[input_list[j]] = input_list[j + 1]


    # for i in range(E+1):



