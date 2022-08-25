N = int(input())

num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    if i == 0:
        maximum = num_list[i]
    else:
        if maximum < num_list[i]:
            maximum = num_list[i]
        else:
            pass
    if i == 0:
        minimum = num_list[i]
    else:
        if minimum > num_list[i]:
            minimum = num_list[i]
        else:
            pass
print(minimum, maximum, end=" ")