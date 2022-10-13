# def isvalid2(arr, k):
#     '''
#     소거법
#
#     :param arr:
#     :param k:
#     :return:
#     '''
#     visited = [0]*(size+2)
#     for i in range(1, size+1):
#         if abs(arr[i] - arr[i+1]) > 1:
#             return False


def isvalid(arr, k):
    '''
    :param arr: 검사 원하는 일렬로 된 땅(높이로 이어짐) 6~20길이
    :param k: 보강판 길이 (slope) 2~4
   :return:true/ false가능한지
    '''
    end = len(arr)
    print(f'before{arr}')
    i = 1 # 1~ N번 idx까지 비교할거임. 0, N+1은 더미로 채웠으니
    for i in range(1, size):
        if abs(arr[i] - arr[i+1]) > 2:
            print('action')
            return False

        if abs(arr[i] - arr[i+1]) == 2 and not arr[i]%2: # 높이차이가 1(2배)이고, 경사로 건설이 안되어있다면
            if arr[i] > arr[i+1]:
                for j in range(i+1, i+k+1):
                    if 0 <= j < end:
                        arr[j] += 1
                    else:
                        print('bring next arr. you touched edge element1')
                        return False
            else:
                for j in range(i, i-k-1, -1):
                    if 0 <= j < end:
                        arr[j] += 1
                    else: # 테두리를 건드린다 -> 바로 짤.
                        print('bring next arr. you touched edge element2')
                        return False
    if arr[-1] == 0:
        print('bring next arr. you touched last element')
        return False

    for k in range(1, size):
        if abs(arr[k] - arr[k + 1]) >= 2:
            print('bring next arr. gap is exceeded')
            return False
    print(f'done: {arr}')
    return True




T = int(input())



for case in range(1, T+1):

    size, slope = map(int, input().split())
    ground = [[-1] + list(map(lambda x: x*2, map(int, input().split()))) + [-1] for _ in range(size)]
    ground = [[-1]*(size+2)] + ground + [[-1]*(size+2)]
    zip_ground = list(map(list, zip(*ground)))

    cnt = 0
    for x in range(1, size+1):
        if isvalid(ground[x], slope):
            cnt += 1
        if isvalid(zip_ground[x], slope):
            cnt += 1

    print(f'#{case} {cnt}')