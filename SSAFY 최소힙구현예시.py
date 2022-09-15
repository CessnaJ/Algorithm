heap = ['최소힙:']

def heap_push(item):
    heap.append(item) # 완전 이진트리니까 맨 끝에 원소를 넣는다.

    child_idx = len(heap)-1
    parent_idx = child_idx // 2 # 부모를 구하기 위해 자식 인덱스에서 floor 연산을 한다.

    while parent_idx and heap[parent_idx] > heap[child_idx]: #루트노드 아니고, 위를 봤는데 더 큰게 있으면 반복된다.
                    # 부모가 없는 최상단 노드가 될때까지. and 최소힙이니까 parent가 더 커서 바꿀게 있을때 계속 반복
                    # root가 되어 더 위에꺼가 없거나, 최소힙 모양이 잘 되어있으면 while이 터진다.
        heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]

        child_idx = parent_idx # 바꾸고나서는 idx도 계속 추적해서 그 뒤랑 또 비교해줘야되니까 chile_idx를 parent_idx로 갱신해주고,
        parent_idx = child_idx//2 # 새로운 parent_idx는 바뀐 child의 //2라는 뜻. 완전2진트리의 성격.



def heap_pop():
    if len(heap) == 1: # 비어있는 상태에서 pop이 일어나지 않게..
        return


    result = heap[1]
    item = heap.pop() # 맨 마지막꺼(제일큰거)를 일단 root에 옮기고 그 다음에 다시 대소비교해서 스왑으로 정렬해주기로 했잖아.
    heap[1] = item

    parent_idx = 1 # 루트시작이니까 1로 지정.
    child_idx = parent_idx *2 # 일단 왼쪽이 작다고 가정 (오른쪽이 없을수도 있기에)

    if child_idx +1 <= len(heap) -1: #오른쪽이 존재할때~(완전이진트리니까 len-1이 마지막 노드의 idx임)
        if heap[child_idx] > heap[child_idx+1]: #왼쪽이 오른쪽보다 크면! 더 작은애를 끌어올려야되니까 오른쪽 선택!
            child_idx += 1

    # 아래로 내려가니까 오른쪽 node가 존재할때까지 and
    # 최소힙 유지를 위해 필요할때까지
    while child_idx <= len(heap)-1 and heap[parent_idx]>heap[child_idx]: #동작조건- 크기만족해서 바꾸는거 가능 & 부모가 더 커서 바꿀 건덕지가 있다.

        heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
        parent_idx = child_idx
        child_idx = parent_idx*2

        if child_idx +1 <= len(heap)-1:
            if heap[child_idx] >heap[child_idx+1]:
                child_idx += 1

    return result





    return result