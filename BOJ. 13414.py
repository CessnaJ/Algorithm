# accommodate, students = map(int, input().split())
# submit = list()
# duplicate = set()
# for _ in range(students):
#     new_input = input()
#     if new_input not in duplicate:
#         submit.append(new_input)
#         duplicate.add(new_input)
#     else:
#         submit.remove(new_input)
#         submit.append(new_input)
# print(*submit[:accommodate], sep='\n')
# # 그래 이렇게 될리가 없지. hash를 이용. priority개념이 들어가야할거같다.
# ----------------------------------------------------------------------------------
#
#
# from collections import defaultdict # dict의 성질- 순서가 있음. key 따라서 순회가 가능.
#
# accommodate, students = map(int, input().split())
# id_priority_dict = defaultdict(int) # 1 이면 최고의 우선순위임. 동일 밸류에서 우선순위는 들어간 순서로.
#
# for _ in range(students):
#     new_input = input()
#     id_priority_dict[new_input] += 1
#
# ordered_id_count = sorted(list(id_priority_dict.items()), key=lambda x: x[1])
#
# for idx in range(accommodate):
#     print(ordered_id_count[idx][0])

#
# ---------------------------------------------------------------------------------------------
# 왜 안되?

from collections import defaultdict  # dict의 성질- 순서가 있음. key 따라서 순회가 가능.

accommodate, students = map(int, input().split())
id_priority_dict = defaultdict(int) # 1 이면 최고의 우선순위임. 동일 밸류에서 우선순위는 들어간 순서로.
count = 0
for _ in range(students):
    new_input = input()
    id_priority_dict[new_input] = count
    count += 1


ordered_id_count = sorted(id_priority_dict.keys(), key=lambda x: id_priority_dict[x])
print(*ordered_id_count[:accommodate], sep='\n')


# -------------------------------------------------------------------------------------------
# import sys
# from collections import defaultdict  # dict의 성질- 순서가 있음. key 따라서 순회가 가능.
#
# accommodate, students = map(int, input().split())
# id_priority_dict = defaultdict(int) # 1 이면 최고의 우선순위임. 동일 밸류에서 우선순위는 들어간 순서로.
#
# id_list = [sys.stdin.readline().strip() for _ in range(students)]
# count = 0
# for new_input in id_list:
#     id_priority_dict[new_input] = count
#     count += 1
#
# ordered_id_count = sorted(id_priority_dict.keys(), key=lambda x: id_priority_dict[x])
# print(*ordered_id_count[:accommodate], sep='\n')
# #