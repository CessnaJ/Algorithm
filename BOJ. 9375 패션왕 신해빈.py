T = int(input())           # swea랑 비슷한 형식

for case in range(1, T+1):
    items = int(input())   # 몇개인지?
    item_sort_dict = {}    # 이쁘게 key-value로 담을 dict 정의

    for _ in range(items):
        item = input().split() # 분리시켜서 리스트로 임시로 저장
        if not item_sort_dict.get(item[1]): # 1번 idx가 분류, 0번 idx가 아이템이름. get은 오류가 안뜨는 method.
            item_sort_dict[item[1]] = [item[0]] # 비어있으면 일단 하나 list형으로 채워넣어서 정의해줌.
        else:
            item_sort_dict[item[1]].append(item[0]) # 비어있지않다면 기존 list형 value에 append
    if not items:                                   # 조건 보면 n이 0일수도 있어
        print(0)
    else:
        answer = 1
        for key in item_sort_dict:                  # 핵심로직. 경우의수 숫자만 구하니까 각 분류별로 안입거나, 하나를 입거나(length +1)
            answer *= (len(item_sort_dict[key])+1)  # 해서 그 숫자를 누적곱 시켜줌.
        print(answer-1)                             # 뭐라도 입어야하니 공집합은 제외. 출력.








