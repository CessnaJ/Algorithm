# 입력 받아서 asc로 정렬하고, brute force로 풀면 10분컷일듯? 2시 5분 시작! 또 코드 순서 잘못해서 20분 걸림
# 정렬 안해도 되는데 그냥 하자! 다시보니 오름차순 출력하라고 하니까 정렬을 미리 해두면 깔끔할듯
dwarf_list = [int(input()) for _ in range(9)]
dwarf_list_asc = sorted(dwarf_list) # 다 쓰기 귀찮다. 어차피 조건은 9마리 준거고, 2개 빼면 되니까~ 빼는걸로 진행하자. 이렇게 해도 bruteforce다.

# for i in range(9):
#     dwarf_list_dsc = dwarf_list_asc[::-1] # refresh 위함.
#     one_out = dwarf_list_dsc.remove(dwarf_list_dsc[i])
#     for j in range(8):
#         two_out = dwarf_list_dsc.remove(one_out[j])
#         if sum(two_out) == 100:
#             print(*sorted(two_out), sep='\n')

end_it = False # 사실 while로 해야 더 깔끔.
for i in range(9):
    dwarf_list_dsc = dwarf_list_asc[::-1] # refresh 위함. # 얕은 복사 쓰면서 reverse 편하게 가자.
    dwarf_list_dsc.remove(dwarf_list_dsc[i])
    for j in range(8):
        temp_dwarf = dwarf_list_dsc.pop(j)
        # dwarf_list_dsc.remove(dwarf_list_dsc[j])
        for_me = sum(dwarf_list_dsc)
        if sum(dwarf_list_dsc) == 100:
            end_it = True
            print(*sorted(dwarf_list_dsc), sep='\n')
            dwarf_list_dsc.insert(j, temp_dwarf)
            break
        else:
            dwarf_list_dsc.insert(j, temp_dwarf)
    if end_it:
        break
