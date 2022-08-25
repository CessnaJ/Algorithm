# 핵심아이디어 -> list에 한글자씩 떼서 변환하고(ASCII 이용) join으로 합친다.
reverse_num_list = []
count = 0
num = -39000000000

while num //10: # 0 될 때 까지 반복. Truthy Falsy 이용.
    # 먼저 자리수 파악한다.
    while count

    reverse_num_list.append(num % 10)
    num = num // 10
    if num // 10 == 0:
        reverse_num_list.append(num)
    elif num == -1:
        reverse_num_list.append(num)
        num = 0
    print(num)
    print(reverse_num_list)
reverse_char_list = []
for i in reverse_num_list:
    reverse_char_list.append(chr(i + 48))
num_into_str = ''.join(reverse_char_list.reverse())

print(num_into_str)
print(reverse_char_list)
print(reverse_num_list)





# def itoa(num): # 핵심아이디어 -> list에 한글자씩 떼서 변환하고(ASCII 이용) join으로 합친다.
#     reverse_num_list = []
#     while num // 10:  # 0 될 때 까지 반복. Truthy Falsy 이용.
#         reverse_num_list.append(num % 10)
#         num = num // 10
#         if num // 10 == 0:
#             reverse_num_list.append(num)
#     reverse_char_list = []
#     for i in reverse_num_list:
#         reverse_char_list.append(chr(i + 48))
#     num_into_str = ''.join(reverse_char_list.reverse())