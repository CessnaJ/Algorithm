Vertex, Edges = map(int, input().split()) # 얘는 똑같고
keys = list(range(Vertex+1))


new_dict = dict.fromkeys(keys)

for key in new_dict:
    new_dict[key] = []


new_dict[3].append(5)
print(new_dict)


# from collections import defaultdict


