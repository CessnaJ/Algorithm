# 이곳에 코드와 주석을 작성합니다. python 치트키 method 적극활용
# 이거 정렬 사용해야 하는 문제인가요?
# 아이디어 -> 문제에서 원하는건 그냥 개수 뽑아서 space 하나씩 넣어서 나열해달라는것
# 메모장 켜서 보니까 마지막 word 뒤에도 space가 하나 있음.
# default dict 만들어서 counting 한 다음에 그 숫자만큼 공백 끼워넣어서 print하면 문제해결.

T = int(input()) # case 10개 input 받음.
dict_keys = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# default dict 만들기 위한 key list
for case in range(1, T+1):
    useless_input = input()          # 받아도 필요 없어서 안씁니다.
    str_input_data = input().split() # input받은 모든 str을 list로 포장해서 넣음.
    word_counting_dict = dict.fromkeys(dict_keys, 0) # 개수 세주기 위한 기본 dict. test case마다 개수 refresh 기능도 겸하기 위해 여기 위치.
    for i in str_input_data:         # list로 순서 그대로 포장받은거 dict에 개수 세서 넣어주기.
        word_counting_dict[i] += 1
    print(f'#{case}', end='\n')      # 기본양식 맞춰주기 밑에서는 줄바꿈 없게 했으니 여기서 다시 나눠줌.
    for j in dict_keys:              # 핵심코드 - dict를 key로 순회해서, key가 되는 str을 공백하나 붙혀서 해당 개수만큼 (dict의 key로 숫자에 접근)
        print((j + ' ')*word_counting_dict[j], sep='', end='') # 양식 맞춰주기 위해서 sep, end를 알맞게 조정.
