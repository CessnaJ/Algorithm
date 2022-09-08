# 풀기 전 생각!

#작은파일의 크기가 큰 파일의 크기 90%미만 ->넘어가자.
# (Fi, Fj) 쌍을 검사해야 하는데,
# 이때, i≠j이고, size(Fi) ≤ size(Fj)이면서,
# size(Fi) ≥ 0.9 × size(Fj)인 쌍만 검사
# 몇개의 쌍?
# ordered list로 만들고, binary search. 그리고 조건 달거임.

# 다 탐색해서 시간초과가 난다면 어떻게 진행할지 고민을 해보자 우리가 배운 탐색방법들..
# 몇개 없다 ㅋㅋ

how_many = int(input())

file_list = sorted(list(map(int, input().split())))
# ascending order sort

def binarySearch(arr, value):
    # 오랜만에 써봐서 까먹네. start, end, mid는 idx.
    # 값 비교는 idx를 대입해서 적용.
    start = 0
    end = len(arr)-1
    while start <= end:  # start와 end가 교차되면 종료.
        mid = (start + end) //2
        if arr[mid] == 0.9*value: #딱 맞는게 있다.
            return mid   # 원하는 value가 있는 idx를 반환
        elif arr[mid] > 0.9*value:
            end = mid-1
        else:
            start = mid +1
    # 딱 맞는게 없어서 사잇값을 이용해야한다. idx니까 -1이 되는 end를 쓸것이다.
    return start


# 기준이 되는 값이 명확하니까 이게 가능함.

count = 0
for i in range(len(file_list)):
    count += (len(file_list[i:]) - binarySearch(file_list[i:], file_list[i]))


print(count)