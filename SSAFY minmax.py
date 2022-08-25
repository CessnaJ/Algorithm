def find_min(list):
    minimum = list[0]
    for i in list:
        if i < minimum:
            minimum = i
        else:
            pass
    return minimum


def find_max(list):
    maximum = list[0]
    for i in list:
        if i > maximum:
            maximum = i
        else:
            pass
    return maximum

T = int(input())
for case in range(T):
    length_of_list = int(input())
    given_num_list = list(map(int, input().split()))
    min_max = find_max(given_num_list) - find_min(given_num_list)
    print(f'#{case+1} {min_max}')


