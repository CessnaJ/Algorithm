N = int(input())


def conversion(word, end_index):  # 다 보려면 len(word) # 첫글자만 보려면 1
    for index in range(end_index):
        letter = word[index]
        capital_case_letter = letter.upper()
        if capital_case_letter not in shortcut:
            shortcut.append(capital_case_letter)
            word = word[:index] + '[' + word[index] + ']' + word[index + 1:]
            return word  # 이 자체로는 기능이 없음. 바꾼게 새로 넣어졌는지 여부를 확인하기 위한 return/ for loop 도중에 함수 끝낼수도 있음.


shortcut = [' ']
converted = []
for i in range(N):
    new_words = input().split()
    for j in range(len(new_words)):
        whether_converted = conversion(new_words[j], 1)
        if whether_converted:
            new_words[j] = whether_converted
            converted.append(' '.join(new_words))
            break
    else:
        joined_word = ' '.join(new_words)
        whether_converted2 = conversion(joined_word, len(joined_word))
        if whether_converted2:
            converted.append(whether_converted2)
        else:
            converted.append(joined_word)
print(*converted, sep='\n')



a = {''}
a.

    #
    # if len(new_words) == 1:
    #     if not conversion(new_words[0], len(new_words[0])):
    #         converted.append(new_words[0])
    # else:
    #     if conversion(new_words[0], 1):  # if문을 읽어나가는 과정에 변환가능하면 이미 append 액션이 취해지니까
    #         new_word = converted.pop()  # 다시 빼서
    #         converted.append(new_word + ' ' + new_words[1])  # 합쳐진걸 다시 넣어줌
    #         continue
    #     elif conversion(new_words[1], 1):
    #         new_word = converted.pop()
    #         converted.append(new_words[0] + ' ' + new_word)
    #         continue
    #
    #     new_word_str = new_words[0] + ' ' + new_words[1]
    #     if not conversion(new_word_str, len(new_word_str)):
    #         converted.append(new_word_str)




