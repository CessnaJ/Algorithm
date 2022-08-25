T = int(input())
# 다른거 먼저 풀고 함수형으로 refactoring 해볼게요..
for case in range(1, T+1):
    matrix_size, word_length = map(int, input().split())
    word_matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
    match_count = 0
    for row in range(matrix_size):
        consecutive_num = 0
        for col in range(matrix_size):
            if word_matrix[row][col] == 0:
                if word_length == consecutive_num:
                    match_count += 1
                consecutive_num = 0
            else:
                consecutive_num += 1
        else: #마지막이 1이라서 refresh 안되고, match count도 비교 안하는 경우.
            if word_matrix[row][matrix_size-1] and word_length == consecutive_num: # 1인지, 길이 맞는지 체크.
                match_count += 1 # 어차피 위에서 consecutive 갱신됨.
    word_matrix = list(zip(*word_matrix))

    for row in range(matrix_size):
        consecutive_num = 0
        for col in range(matrix_size):
            if word_matrix[row][col] == 0:
                if word_length == consecutive_num:
                    match_count += 1
                consecutive_num = 0
            else:
                consecutive_num += 1
        else: #마지막이 1이라서 refresh 안되고, match count도 비교 안하는 경우.
            if word_matrix[row][matrix_size-1] and word_length == consecutive_num: # 1인지, 길이 맞는지 체크.
                match_count += 1 # 어차피 위에서 consecutive 갱신됨.
    print(f'#{case} {match_count}')


# word_matrix = [input().replace(' ', '') for _ in range(matrix_size)] #이거 그냥 문자열로 받아서 연속된 1의 개수가 맞으면 row 에 있다고 출력할것.
#
# for row in range(matrix_size):
#     if '1'*word_length in word_matrix[row]:
#         print(f'#{} {row + 1}')

