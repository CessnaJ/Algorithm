height, width = map(int, input().split())
terrains = list(enumerate([0]+ list(map(int, input().split())) + [0])) # list니까 억지로 s 붙힘/ idx 0~width+1
waters = [0]*width



peak_ready = False
for i in range(width+1):
    if terrains[i][1] < terrains[i+1][1]: # 상승중!
        peak_ready = True
    elif terrains[i][1] > terrains[i+1][1] and peak_ready: # 하락했고 상승중이었으면 peak를 뜻함.
        peak_ready = False
        current_peak = terrains[i][0]
