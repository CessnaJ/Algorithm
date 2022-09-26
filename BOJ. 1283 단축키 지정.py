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