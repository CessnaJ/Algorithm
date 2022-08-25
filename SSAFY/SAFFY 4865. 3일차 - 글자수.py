T = int(input())

for case in range(1, T+1):
    piece = input()
    full_str = input()
    dict_for_counting = dict.fromkeys(piece, 0)

    for key in dict_for_counting:
        for letter in full_str:
            if key == letter:
                dict_for_counting[key] += 1
    max_duplicate = 0
    for key in dict_for_counting:
        if dict_for_counting[key] > max_duplicate:
            max_duplicate = dict_for_counting[key]

    print(f'#{case} {max_duplicate}')