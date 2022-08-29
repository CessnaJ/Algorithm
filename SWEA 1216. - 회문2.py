def palindrome_test(string):
    if string == string[::-1]:
        return len(string), string

T = 10

for case in range(1, T+1):
    input()
    matrix = [input() for _ in range(100)]
    matrix_t = list(zip(*matrix))
    palindrome_list = []

    for row in range(100):
        for start_col in range(99):
            for end_col in range(start_col+2, 101):
                if palindrome_test(matrix[row][start_col: end_col]):
                    palindrome_list.append(palindrome_test(matrix[row][start_col: end_col]))

    for row in range(100):
        for start_col in range(99):
            for end_col in range(start_col+2, 101): # 이거 100으로 해서 하나 틀렸음. 하나 틀린게 아니라 그냥 틀린거임. 마지막 idx를 제거하고 보는거니까. 100줄짜리를 idx로 탐색하려면 101줄을 봐야함.
                if palindrome_test(matrix_t[row][start_col: end_col]):
                    palindrome_list.append(palindrome_test(matrix_t[row][start_col: end_col]))
    sorted_palindrome_list = sorted(palindrome_list, key=lambda x: x[0])

    print(f'#{case} {sorted_palindrome_list[-1][0]}')
