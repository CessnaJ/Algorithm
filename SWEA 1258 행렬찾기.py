# 어떻게 풀것인가? idx 0행을 제외하고는 분리되어있다는것이 왼쪽에 0이 존재한다는 의미가 될것이다.
# 열도 동일하게 위에 idx 0열을 제외하고는 위쪽에 0이 존재한다는 의미가 될것이다.
# 한번 돌려서 기준 idx[row][col]를 for loop 돌리고, 한번 뭔가 기준이 될 idx를 발견하면, 행 탐색을 통해서 0이 시작되는 지점을
# 카운팅하고, 열탐색을 시작해서 0이 시작되는 지점을 카운팅해서 행,열 데이터를 삽입한다.
# 그리고 visited list에 해당 사각형을 방문처리해서 loop에서 벗어나게한다.(이걸 함수를 통해서 모양 만들기함.)
# 마지막에 행렬 곱한거 비교해서 버블정렬로 정렬한다음에,
def color_the_matrix(start_idx, matrix_before_coloring):
    col_count = 0
    row_count = 1 # 얘는 1을 해줘야 오류가 안생긴다 col이랑은 다른게, 일단 loop를 들어가면서 첫 for loop은 col 위해서 회피해야되니까.

    search_row_only = False
    for row_inside in range(start_idx[0], matrix_size):
        if search_row_only:
            if chemical_matrix[row_inside][start_idx[1]]:
                row_count += 1 # 첫번째 열만 탐색하면 되니까. 이게 플래그가 서고나서, 후순위 로직인데 먼저 가는게 맞아서 이렇게..
                continue
            else:
                break # 0이 나왔다는 말이다. 큰 for loop 파괴.
        else:
            for col_inside in range(start_idx[1], matrix_size):
                if chemical_matrix[row_inside][col_inside]: #한번 탐색시작하면 거기서부터는 연속되서 쭈우욱 카운트 될거임.
                    col_count += 1
                else: # 한번이라도 0이 나오면 그냥 깽판치고 col 반환할거니까. 문제에서 원하는건 행렬의 '크기' 뿐이다.
                    search_row_only = True
                    break # 플래그를 세우고나서 col탐색을 종료한다. 작은 for loop파괴. 이제 열만 보면 됨.
            else:
                search_row_only = True # 끝까지 0이 안나왔을때를 위해 추가.

    end_row = start_idx[0] + row_count # 이미 자기 자신도 카운트대상에 들어가니까 마지막 idx에 넣으면 자연스레 1이 빠짐.
    end_col = start_idx[1] + col_count # 이하 같음.
    for row_inside2 in range(start_idx[0], end_row):
        for col_inside2 in range(start_idx[1], end_col):
            matrix_before_coloring[row_inside2][col_inside2] = 1 # 다 끝나고 색칠하는 액션.

    return [row_count, col_count]  # 작은 matrix 사이즈는 return해줘야 함. function의 action과 return을 분리해서 생각하기.


def area(coordinate): # lambda 함수 써서 넣으려고 했는데, php8경고에 외부에서 변수 참조할거면 정의를 따로 하라고 하네요 ㅠㅠ
    return coordinate[0] * coordinate[1]


def bubble_sort_by_size_n_row(coordinate_list):
    for end_idx in range(len(coordinate_list)-1, -1, -1):
        for idx in range(end_idx):
            if area(coordinate_list[idx]) > area(coordinate_list[idx+1]):
                coordinate_list[idx], coordinate_list[idx +1] = coordinate_list[idx+1], coordinate_list[idx]
            elif area(coordinate_list[idx]) == area(coordinate_list[idx+1]):
                if coordinate_list[idx][0] > coordinate_list[idx+1][0]:
                    coordinate_list[idx], coordinate_list[idx + 1] = coordinate_list[idx + 1], coordinate_list[idx]
    return coordinate_list



T = int(input())

for case in range(1, T+1):
    matrix_size = int(input())
    chemical_matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
    visited_matrix = [[0]*matrix_size for _ in range(matrix_size)]
    result_list = []

    for row in range(matrix_size):
        for col in range(matrix_size):
            if not visited_matrix[row][col]: # 0일때 확인. visitied matrix에서 체크된 항목은 이미 확인된 소matrix니까 보지않겠다.
                if chemical_matrix[row][col]: # visited로 확인 안되면서 top/left tip으로 감지되면 해당 idx 기준으로 function call
                    result_list.append(color_the_matrix([row, col], visited_matrix)) # 색칠을 해줄거라서 parameter로 넣는다. namescaping 규칙상, 조작하려면 넣어줘야함. 이런걸로 global 쓰는건 최악.

    result_in_list = bubble_sort_by_size_n_row(result_list)


    print(f'#{case} {len(result_list)}', end=' ')
    for i in result_in_list:
        for j in i:
            print(j, end=' ')
    print(end='\n')
