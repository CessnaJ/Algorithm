target_str= input()                       # str 받음.
censor_char_in_CAMBRIDGE = ['C','A','M','B','R','I','D','G','E'] # CAMBRIDGE의 각 글자를 for loop해서 없애주기 위한 list
for i in censor_char_in_CAMBRIDGE:        # letter 순서로 for loop
    target_str = target_str.replace(i,"") # replace함수 써서 없애버립니다.
print(target_str)                         # 출력