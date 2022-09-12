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

#원하는것. 검사를 안할 기준 idx가 몇인지를 원함. 정렬은 되어있으니 binary search 이용해서 0.9기준값의 idx를 뽑자.
def binarySearch(arr, ref_val): # arr와 기준값을 받아서 기준값 0.9배의 기준이 되는 idx를 반환하는것.
    start = 0
    end = len(arr)-1            # len에서 1을 뺀 마지막 idx
    while start <= end:         # start와 end가 교차되면 종료.
        mid = (start + end) //2
        if arr[mid] >= 0.9 * ref_val: # 가운데를 짚었는데 기준값0.9보다 커. 더 왼쪽으로 간다.
            end = mid - 1
        else:                         # 가운데를 짚었는데 기준값0.9 보다 작아. 더 오른쪽으로 간다.
            start = mid + 1
    # 딱 맞는게 없을때 사잇값 idx를 이용해야한다.
    # 이렇게 되면 결국 교차가 될것임. 교차가 되어서 나오게 되는 start idx를 사용.
    return start
#여기에 i랑 start가 같으면 start-1부터 카운팅하는걸로 하자.

# 생각해볼점.
# 가운데를 딱 짚었는데 0.9이고, 왼쪽 오른쪽 다 같은값으로 0.9배인게 여러개 있으면 그 첫 idx를 짚어내야지?(그러니까 '이상'이면 왼쪽으로 계속 가서 안되는 그 틈새를 찾아야함)
count = 0
for i in range(len(file_list)-1, 0, -1): # max idx값부터 1까지 i로 대입.
    count += (i - binarySearch(file_list[:i], file_list[i]))
    # i는 포함안되는 list에서 검사. 그리고 ref_value는 i번째.
print(count)
# files_to_check = file_list[:i]
# count += (i - binarySearch(files_to_check, files_to_check[-1]))