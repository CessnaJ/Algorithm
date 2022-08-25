# 조건-> 원하는 나무 총 M미터. N 나무개수.
# H는 설정한 벌목 기준 높이

N, M = map(int, input().split()) # list가 N개의 원소. 원하는 나무의 길이M
lumber_idx_list = enumerate(sorted(list(map(int, input().split())))) # 나무길이 asc로 정렬된 enumerate list. len씌우면 N일것이다.

def negative_binary_search():
    pass


def positive_binary_search():
    pass







def idx_finder(V):
    if V%2:
        V = V//2
    else:
        V = V//2 - 1

N = N//2 if N%2 else N//2-1 #3항연산자 이용 원소개수 홀짝별로 나눠서 이진탐색 자를 위치를 정함. 이걸 anchor_idx라고 함.
anchor_idx = N # 말로 쓰고 싶은데 새로 메모리 할당안하고 포인터 지정해줘서 이렇게
whether_to_try = 0 #인덱스 기준으로 했을때, 범위를 좁혀나가야하는데,
# 해당 idx의 높이로 H를 잡으면 그 idx기준으로 최대 나무길이가 나옴. 만약 이게 M에 못미친다면, idx를 잘못잡은것. 맞다면 여기서 점점 좁혀나감.

if sum(lumber_list[anchor_idx:]) - sum(len(lumber_list[anchor_idx:]) * lumber_list[anchor_idx])< M: #idx잘못잡아서 가장 막내 나무로 톱대도  원하는 수치 못미침 더 많은 나무를 잘라야함.
    pass


print(H)