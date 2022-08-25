bingo = []
call = []
combo = 0

while len(bingo) == 5:
    bingo.append(list(map(int,input().split())))

while len(call) == 25:
    call.extend(list(map(int,input())))

for i in call:
    for j in range(5):
        for k in range(5):
            if i == bingo[j][k]:
                bingo[j][k] = 0
                if bingo[j] == [0, 0, 0, 0, 0]:            #가로빙고체크
                    combo += 1
                elif j == k:
                    for l in range(5):              # 왼오대각선빙고체크
                        if bingo[l][l] != 0:
                            continue
                    else:
                        combo += 1