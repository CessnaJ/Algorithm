# 틀렸음. 다시 해야됨.일반적인 경우로 다시 받아서 쓰는걸 추천한다. 4개라서 이렇게 만들었는데, 이렇게 해봤자 더 편하지도 않고 case 분류하느라 짜증만남.


def rotate(gear, direction):
    global new_index1, new_index2, new_index3, new_index4, index1, index2, index3, index4
    if gear == 'gear1':
        new_index1 = (index1 - direction) % 8
        if gear1[(index1 + 2)%8] != gear2[index2 - 2]:
            new_index2 = (index2 + direction) % 8
            if gear2[(index2 + 2)%8] != gear3[index3 - 2]:
                new_index3 = (index3 - direction) % 8
                if gear3[(index3 + 2)%8] != gear4[index4 - 2]:
                    new_index4 = (index4 + direction) % 8
    if gear == 'gear4':
        new_index4 = (index4 - direction) % 8
        if gear3[(index3 + 2)%8] != gear4[index4 - 2]:
            new_index3 = (index3 + direction) % 8
            if gear2[(index2 + 2)%8] != gear3[index3 - 2]:
                new_index2 = (index2 - direction) % 8
                if gear1[(index1 + 2)%8] != gear2[index2 - 2]:
                    new_index1 = (index1 + direction) % 8

    if gear == 'gear2':
        new_index2 = (index2 - direction) % 8
        if gear1[(index1 + 2)%8] != gear2[index2 - 2]:
            new_index1 = (index2 + direction) % 8
        if gear2[(index2 + 2)%8] != gear3[index3 - 2]:
            new_index3 = (index3 + direction) % 8
            if gear3[(index3 + 2)%8] != gear4[index4 - 2]:
                new_index4 = (index4 - direction) % 8
    if gear == 'gear3':
        new_index3 = (index3 - direction) % 8
        if gear3[(index3 + 2)%8] != gear4[index4 - 2]:
            new_index4 = (index4 + direction) % 8
        if gear2[(index2 + 2)%8] != gear3[index3 - 2]:
            new_index2 = (index2 + direction) % 8
            if gear1[(index1 + 2)%8] != gear1[index1 - 2]:
                new_index1 = (index1 - direction) % 8
    index1 = new_index1
    index2 = new_index2
    index3 = new_index3
    index4 = new_index4





T = int(input())

for case in range(1, T+1):
    K = int(input())
    gear1 = list(map(int, input().split()))
    gear2 = list(map(int, input().split()))
    gear3 = list(map(int, input().split()))
    gear4 = list(map(int, input().split()))
    index1 = new_index1 = 0
    index2 = new_index2 = 0
    index3 = new_index3 = 0
    index4 = new_index4 = 0
    for _ in range(K):
        gearNo, rotation = map(int, input().split())
        rotate(f'gear{gearNo}', rotation)

    answer = sum([gear1[new_index1], gear2[new_index2]*2, gear3[new_index3]*4, gear4[new_index4]*8])

    print(f'#{case} {answer}')