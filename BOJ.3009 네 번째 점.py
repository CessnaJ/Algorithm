input_list = [list(map(int, input().split())) for _ in range(3)]
ans = []
for i in zip(*input_list):
    if i[0] == i[1]:
        ans.append(i[2])
    elif i[1] == i[2]:
        ans.append(i[0])
    else:
        ans.append(i[1])
print(*ans, sep=" ")