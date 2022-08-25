'''
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

다음과 같은 5X5 배열에서 최댓값은 29이다.


'''

for _ in range(10):
    case_num = int(input())
    given_matrix = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    temp_sum1 = 0
    temp_sum2 = 0
    temp_sum3 = 0
    temp_sum4 = 0
    for row in range(100):
        temp_sum1 += given_matrix[row][99-row]
        temp_sum2 += given_matrix[row][row]
        for col in range(100):
            temp_sum3 += given_matrix[row][col]
            temp_sum4 += given_matrix[col][row]
        else:
            if temp_sum3 > max_sum:
                max_sum = temp_sum3
            if temp_sum4 > max_sum:
                max_sum = temp_sum4
            temp_sum3 = 0
            temp_sum4 = 0
    if temp_sum1 > max_sum:
        max_sum = temp_sum1
    if temp_sum2 > max_sum:
        max_sum = temp_sum2
    print(f'#{case_num} {max_sum}')
