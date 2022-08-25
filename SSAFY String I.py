
# list slicing으로 하는건 많이 해봤으니 string으로 해결해볼까 했는데, 어차피 str object는 immutable하기때문에
# 제가 뭔가를 할때마다 memory에서 생성하고 지우는걸 반복할것이기에 list로 해결합니다.

original_str = input('Type in the string that you wanna make palindrome: ')
char_list = []
char_list_reverse = []
for i in original_str:
    char_list.append(i)

for j in range(len(char_list)-1, -1, -1):
    char_list_reverse.append(char_list[j])

palindrome_str = ''.join(char_list_reverse)

print(palindrome_str)
