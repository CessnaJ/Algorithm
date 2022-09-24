# input - N(1~30)명
# M (3~30)치킨 종류 수
# N개의 row, M개의 col 각 row는 M개의 메뉴들에 대한 각 사람의 만족도

N, M = map(int, input().split()) # 받아오는 input N= 사람숫자&row 개수, M=메뉴개수에 대한 각 만족도&col
satisfaction = [list(map(int, input().split())) for _ in range(N)] #2차원 배열로 받음.

max_satisfaction = [0]
for i in range(M): # 1번 후보
    for j in range(i+1, M): # 2번 후보
        for k in range(j+1, M): # 3번 후보
            temp = 0
            for person in range(N): # 행(사람) 순회
                temp += max(satisfaction[person][i], satisfaction[person][j], satisfaction[person][k]) # row 순회 하면서 3개 고른것중에 최고
            max_satisfaction.append(max(temp, max_satisfaction[-1])) # 최대치를 list의 마지막index로. list가 상당히 길어질듯 ㅋㅋ
print(max_satisfaction[-1]) # 맨 마지막에 오는게 최대치일테니. 그냥 고치는거랑 실행시간 똑같음. 실험해봄.



#             if temp > max_satisfaction: # 더한게 최대값보다 높으면
#                 max_satisfaction = temp # 치환
# print(max_satisfaction)