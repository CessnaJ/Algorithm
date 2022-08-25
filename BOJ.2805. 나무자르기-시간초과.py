# 조건-> 원하는 나무 총 M미터. N 나무개수.
# H는 설정한 벌목 기준 높이

N, M = map(int, input().split())   # list가 N개의 원소. 원하는 나무의 길이 M
list_of_tree = list(map(int, input().split()))  # 나무의 높이를 받는다.

start, end = 1, max(list_of_tree)  # 시작 높이, 끝 높이
while start <= end: # end가 더 크면 안되지.
    mid = (start + end) // 2  # 높이에 대한 binary search 사용
    temporary_log_length = 0  # 잘린 나무의 임시 길이
    for tree in list_of_tree:
        if tree >= mid:  # mid보다 큰 나무라면 잘라서 temp에 누적합 시켜줌.
            temporary_log_length += (tree - mid)
    if temporary_log_length >= M:  # 목표 나무 길이보다 크다면 절단기 1씩 높혀준다.
        start = mid + 1
    else:  # 목표 나무 길이보다 작다면 1씩 절단기 낮춰준다.
        end = mid - 1

print(end)

# 이거 시간초과.. 하아.. 결국 2분탐색을 더 정확하게 쓰기 위해서 sorted list를 이용해볼수있을까?