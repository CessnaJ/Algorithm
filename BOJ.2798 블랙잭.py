N, M = map(int, input().split())
card_list = list(map(int, input().split()))
max_val = 0
for i in range(len(card_list)):
    for j in range(len(card_list))[i+1:]:
        for k in range(len(card_list))[j+1:]:
            if max_val < card_list[i] + card_list[j] + card_list[k] <= M:
                max_val = card_list[i] + card_list[j] + card_list[k]
            else:
                pass
print(max_val)
