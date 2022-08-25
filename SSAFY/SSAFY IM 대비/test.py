# num_of_switch = 45
# switch_input = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1,]
#
# for a in range(num_of_switch):
#     if a!=0 and a % 20 == 0:
#         print(end='\n')
#     print(switch_input[a], sep='', end=' ')

print(list(enumerate(map(int, input().split()))))