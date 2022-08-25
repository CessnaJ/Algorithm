N = int(input())
input_list = input().split()
num_list = []

for i in input_list:
    i = int(i)
    num_list.append(i)

sorted_num_list = sorted(num_list)
median = int((N+1)/2)
print(sorted_num_list[median-1])