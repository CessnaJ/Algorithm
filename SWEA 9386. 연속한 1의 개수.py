T = int(input())

for case in range(T):
    letter_length= int(input())
    given_num_str = input()
    count = 0
    max_count = 0
    for i in given_num_str:
        if i == '1':
            count += 1
        else:
            if count > max_count:
                max_count = count
                count = 0
    else:
        if count > max_count:
            max_count = count
        count = 0
    print(f'# {case + 1} {max_count}')