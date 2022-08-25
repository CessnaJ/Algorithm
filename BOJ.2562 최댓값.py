list = []
for i in range(9):
    n = int(input())
    list.append(n)

for k,v in enumerate(list):
    if k == 0:
        max_num = list[0]
        idx = k
    else:
        if list[k] > max_num:
            max_num = list[k]
            idx = k
        else:
            pass
print(max_num, idx+1, sep='\n')