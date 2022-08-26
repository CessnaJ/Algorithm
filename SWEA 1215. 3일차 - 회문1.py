
T = 10

def is_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

for case in range(1, T+1):
    N = int(input())
    str_list = [input() for _ in range(8)]
    count = 0
    for row in str_list: #가로 비교.
        for start in range(8-N + 1):
            if is_palindrome(row[start:start+N]):
                count += 1

    str_list_t = zip(*str_list)
    for col in str_list_t: # 세로 비교
        for start in range(8-N +1):
            if is_palindrome(col[start:start+N]):
                count += 1

    print(f'#{case} {count}')
