s = "one4seveneight"

# conversion_dict = {'one': '3 1',
#                    'two': '3 2',
#                    'three': '5 3',
#                    'four': '4 4',
#                    'five': '4 5',
#                    'six': '3 6',
#                    'seven': '5 7',
#                    'eight': '5 8',
#                    'nine': '4 9',
#                    'zero': '4 0'}  # 각 숫자에 대응되는 글자수(list scling 이용해서 바꿀 글자수, 무슨 숫자인지를 한번에. 어차피 바꾼 단어도 str이고 마지막에 int로 바꿔줄거라서 이렇게 하는게 편할듯.)
# for i in conversion_dict:
#     start_idx = s.find(i)  # dict의 key를 대입해서 index가 나옴.
#     if start_idx != -1:  # 찾았다면~ conversion_dict[i= one]가 예를 들어서 '3 1' 이렇게 나올테니까
#         s[start_idx: start_idx + int(conversion_dict[i][0])] = conversion_dict[i][2]  # start idx부터 n글자를 문자열인 해당 숫자로 바꿀것이다.
# ''.replace()
# # str은 slicing으로 바꿀수가 없다. immutable object
# answer = int(s)
# print(answer)




conversion_dict = {'one': '3 1',
                   'two': '3 2',
                   'three': '5 3',
                   'four': '4 4',
                   'five': '4 5',
                   'six': '3 6',
                   'seven': '5 7',
                   'eight': '5 8',
                   'nine': '4 9',
                   'zero': '4 0'}  # 각 숫자에 대응되는 글자수(list scling 이용해서 바꿀 글자수, 무슨 숫자인지를 한번에. 어차피 바꾼 단어도 str이고 마지막에 int로 바꿔줄거라서 이렇게 하는게 편할듯.)
for i in conversion_dict:
    start_idx = s.find(i)  # dict의 key를 대입해서 index가 나옴.
    if start_idx != -1:  # 찾았다면~ conversion_dict[i= one]가 예를 들어서 '3 1' 이렇게 나올테니까
        s[start_idx: start_idx + int(conversion_dict[i][0])] = conversion_dict[i][2]  # start idx부터 n글자를 문자열인 해당 숫자로 바꿀것이다.

answer = int(s)



# conversion_dict = {'one': '1',
#                    'two': '2',
#                    'three': '3',
#                    'four': '4',
#                    'five': '5',
#                    'six': '6',
#                    'seven': '7',
#                    'eight': '8',
#                    'nine': '9',
#                    'zero': '0'}
# for i in conversion_dict:
#     s = s.replace(i, conversion_dict[i])
#     print(s)
# return int(s)
