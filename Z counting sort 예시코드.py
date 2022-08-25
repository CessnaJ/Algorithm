# # O(n+k) -> n은 list 길이. k는 최대숫자.
# # 숫자별로 지정을해서 비복원 정렬을 하기 때문에, 최대숫자가 커지면, 그만큼 공간복잡도가 커진다. 얼마나 떨어져있냐. min과 max가.
# arr = [0,2,6,4,7,0,7]
# N = int(input())
#
# arr = list(map(int, input().split()))
#
# temp = [0]*N
# c = [0]*101
# for i in range(N): #숫자 카운팅 일단.
#     c[arr[i]] += 1
#
# for j in range(1, 101): # 개수 누적합. 점점 커짐.
#     c[j] += c[j-1]
#
# for i in range(N-1, -1, -1): # 원본을 뒤에서 읽으면서 정렬결과를 temp에 저장.
#     c[arr[i]] -= 1 # idx로 바뀜. 개수에서 1개를 뺴니까!
#     temp[c[arr[i]]] = arr[i]
# print(c)


# bit masking
# 비트를 활용한 부분집합 구하기
letters = ['a', 'b', 'c']

for i in range(1 << len(letters)):  # 총 2³, 8개의 경우의 수 체크
    selected = []
    for j in range(len(letters)): # 셀로판지가 가야하는 길이는 3
        if i & (1 << j):  # 1칸씩 왼쪽으로 옮겨가며 총 3칸을 대조해본다.
            selected.append(letters[j])

    print(selected)

