# from collections import defaultdict

N = int()


# countdict = defaultdict()
countset = set('ChongChong')


for _ in range(N):
    froma_tob = input().split()
    if froma_tob[0] in countset:
        countset.add(froma_tob[1])
    if froma_tob[1] in countset:
        countset.add(froma_tob[0])
print(len(countset))