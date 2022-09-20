full_str = input()
partial_str = input()
# print(1 if partial_str in full_str else 0)

start_idx = 0
end_idx = start_idx + len(partial_str) - 1 # idx니까 -1을 해줘야 함
str_to_check = full_str[start_idx: end_idx + 1]


for _ in range(len(full_str)-len(partial_str)+1): #
    if str_to_check == partial_str:
        print(1)
        break

    end_idx += 1
    if end_idx == len(full_str):
        continue
    else:
        str_to_check = str_to_check[1:] + full_str[end_idx]
else:
    print(0)



