T = int(input()) # case 몇개?

for case in range(1, T+1):   # 형식 맞춰주기
    palindrome = ''          # refresh
    matrix_size, palindrome_size = map(int, input().split())  # matrix size, palindrome size 받아줌.
    given_string_list = [input() for _ in range(matrix_size)] # list comprehension으로 input 쉽게 받기
    for i in given_string_list:                               # 받아온건 str이 여러개 들어있는 list. 가로방향 비교 시작!
        for j in range(len(i) - palindrome_size + 1):         # 이렇게하면 palindrome size에 맞게 한칸씩 밀면서 비교 가능. 간단한 산수
            test_str = i[j:j+palindrome_size+1]
            if test_str == test_str[::-1]:                    # list slicing을 이용한 대칭 비교.
                palindrome = test_str                         # 맞으면 넣어줌
    if palindrome != '':                                      # 만약 가로 비교해서 회문 찾으면 세로까지 비교할 필요없음.
        print(f'#{case} {palindrome}')
        continue                                              # 대충 끝내고 다음 회차로 넘어간다.

    given_string_list_t = zip(*given_string_list)             # 세로를 비교해줘야하는데 zip을 이용해서 일단 전치.
    for a in given_string_list_t:                             # 위와 동일
        for b in range(len(a) - palindrome_size + 1):         # 위와 동일
            test_str = a[b: b+palindrome_size +1]
            if test_str == test_str[::-1]:
                palindrome = ''                               # zip함수는 iterable들을 치환시켜서 압축해주는데 list안에 tuple들이.
                for k in test_str:                            # 그리고 그 tuple안에는 iterable이 해체되서 들어가는 형태. 이걸 다시 str로 합쳐준다.
                    palindrome += k
    print(f'#{case} {palindrome}')                            # 출력.


