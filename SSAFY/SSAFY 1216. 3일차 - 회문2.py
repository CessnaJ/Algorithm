for case in range(10):
    given_str_list = [input() for _ in range(100)]
    max_palindrome_length = 0
    for length in range(100, 1): # 길이 역순으로 돌리다가 break하는게 낫다.
        for row in range(100):
            for col in range(0, 100-length + 1):
                test_str = given_str_list[row][col:col + length]
                if test_str == test_str[::-1] and len(test_str) > max_palindrome_length:
                    max_palindrome_length = len(test_str)









    print(f'#{case} {ans}')