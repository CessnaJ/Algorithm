# 함수만들어서 검사하고 슬라이딩윈도우로 하나씩 해나가면 시간도 줄일 수 있을듯? 일단 앞뒤가 똑같은지 보고 안되면 끝장내는걸로 시간줄이자.
# 가장 짧은 문자열이면 양끝이 그 문자로 되어있어야하겠지
#
def check_tips(string, chars):
    if string[0] != string[-1]:
        return 0
    else:
        if chars == string.count(string[0]):
            return len(string)
        else:
            return 0

# def check_tips_by_idx(string, start, end):
#     if string[0] != string[-1]:
#         return 0
#     else:
#         if chars == string.count(string[0]):
#             return len(string)
#         else:
#             return 0


T = int(input())

# for case in range(1, T+1): # 시간초과.
#     stringToCheck = input()
#     num = int(input())
#     mincount = 10000
#     maxcount = 0
#     for start in range(len(stringToCheck)):
#         for end in range(start+1, len(stringToCheck)):
#             if 0 < check_tips(stringToCheck[start:end], num) < mincount:
#                 mincount = check_tips(stringToCheck[start:end], num)
#             if maxcount < check_tips(stringToCheck[start:end], num):
#                 maxcount = check_tips(stringToCheck[start:end], num)
#     if mincount == 10000 or maxcount == 0:
#         print(-1)
#     else:
#         print(mincount, maxcount)


# 2번째 방법. 문자열 해체! 그냥 첫번째 문자부터 순회해서 같은 글자가 몇번째 idx에 있는지 쭉 뽑아서 그걸 함수에 넣어버린다.
for case in range(1, T+1):
    stringToCheck = input()
    num = int(input())
    # keys = 'abcdefghijklmnopqrstuvwxyz'
    key_list = list(stringToCheck)
    keys2 = set(key_list)
    matching_len_list = []

    alphabetIdxCorrDict = dict.fromkeys(keys2, None) # 이거 기본값에 []를 넣으니까 같은 객체가 들어가게 됨. id값이 같네요? 그래서 None넣고 일일히 넣어주기로 함.
    for i in alphabetIdxCorrDict: # 일일히 넣기
        alphabetIdxCorrDict[i] = []
    for idx, alphabet in enumerate(stringToCheck): # 주어진 string에서 각 alphabet이 가리키는 idx를 alphabet별로 넣어줌.
        alphabetIdxCorrDict[alphabet].append(idx)


    for key in alphabetIdxCorrDict:
        idxList_forKey = alphabetIdxCorrDict[key]

        if len(idxList_forKey) < num:              # 해당 글자의 개수가 미달이면 검사 할 필요 없음.
            continue
        elif len(idxList_forKey) == num:           # 끝 idx에서 첫 idx를 빼고 1을 더하면 글자의 개수를 뜻하게 됨. 3개짜리 글자를 뽑고싶은데 a가 3개밖에 없는거.
            matching_len_list.append(idxList_forKey[-1] - idxList_forKey[0] + 1)
            # for loop 돌릴필요 없으니까
        else:
            for start in range(len(idxList_forKey)):
                if len(idxList_forKey) > (start + num -1): # 개수가 최대 idx보다 커야겠지? 이런 경우에만 넣어줄거야.
                    matching_len_list.append(idxList_forKey[start + num -1] - idxList_forKey[start] + 1)
    if not matching_len_list:
        print(-1)
    else:
        print(min(matching_len_list), max(matching_len_list)) # 매칭되는건 싹 다 list에 넣었으니 최소숫자, 최대숫자를 출력해주면 됨.



    # print(alphabetIdxCorrDict)

# set으로 합쳐서 빈 알파벳은 검사 안해도 될거같음.



    # for start in range(len(stringToCheck)):
    #     for end in range(start+1, len(stringToCheck)):
    #         if 0 < check_tips(stringToCheck[start:end], num) < mincount:
    #             mincount = check_tips(stringToCheck[start:end], num)
    #         if maxcount < check_tips(stringToCheck[start:end], num):
    #             maxcount = check_tips(stringToCheck[start:end], num)
    # if mincount == 10000 or maxcount == 0:
    #     print(-1)
    # else:
    #     print(mincount, maxcount)