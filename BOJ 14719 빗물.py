height, width = map(int, input().split())
# terrains = list(enumerate([0]+ list(map(int, input().split())) + [0])) # list니까 억지로 s 붙힘/ idx 0~width+1
terrains = list(map(int, input().split()))
waters = [0]*(width)




# peak_ready = False
for i in range(1, width-1):
    left = max(terrains[:i])
    right = max(terrains[i:])
    water_level = min(left, right)
    if water_level >= terrains[i]:
        waters[i] = water_level
print(sum(waters) - sum(terrains[1:width-1]))

# print(sum(terrains))
