# 오늘부터 method를 쓰는데 너무 편하고 행복합니다. 이번에도 str의 한계를 없애주는 치트키인 replace method를 이용합니다.
# 개수만 세면 되죠? Z로 바꿀겁니다.
target_str = input()
whether_croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in whether_croatia_alphabet:
    target_str = target_str.replace(i, 'Z')
print(len(target_str))