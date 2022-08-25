# 하나 call 할때마다 해당 matching block의 숫자를 -1으로 바꾸자.
# 대각선 빙고는 2개밖에 없으니까 따로 테스트하고,
# 정방향 빙고 테스트하고
# zip으로 전치만들어서 전치방향 빙고 테스트 하면 됨.(풀기 전 계획)
# 그렇게 해서 3개 생기면 빙고 외치고 끝나는거

my_bingo = []
bingo_call = []
test = [-1, -1, -1, -1, -1]

num_of_bingo = 0


for i in range(5):
    my_bingo.append(list(map(int, input().split()))) #한줄씩 비어있는 my_bingo에 넣어서 2차원 matrix 생성.

for j in range(5):
    bingo_call.extend(list(map(int, input().split()))) #하나씩 까면 되니까 unpack해서 1차원 matrix로 넣어서 calling list 생성

# my_bingo_t = list(zip(*my_bingo))
my_bingo_t = list(map(list, zip(*my_bingo))) # 전치행렬 만들어준다. tuple형들이 list로 싸여있는거라서 map으로 list만들어줌.

for judge_call_num in bingo_call:
    for i in range(5):
        for j in range(5):
            if my_bingo[i][j] == judge_call_num:
                my_bingo[i][j] = -1 # 새로 맞는게 하나라도 생겼으면 이제 빙고개수 검증들어감.
                my_bingo_t[j][i] = -1 #전치행렬도 바꿔줘야함.
            else:
                continue # 아니면 시간낭비 할 필요 없지. 다음 try로 간다.
            if [my_bingo[0][0], my_bingo[1][1], my_bingo[2][2], my_bingo[3][3], my_bingo[4][4]] == test:
                num_of_bingo += 1 #대각선 테스트
            if [my_bingo[0][4], my_bingo[1][3], my_bingo[2][2], my_bingo[3][1], my_bingo[4][0]] == test:
                num_of_bingo += 1 # 대각선테스트
            for bingo_row in my_bingo: # 순방향 테스트
                if bingo_row == test:
                    num_of_bingo += 1
            for bingo_row in my_bingo_t:# 전치방향 테스트
                if bingo_row == test:
                    num_of_bingo += 1
            if num_of_bingo >= 3: # 갑자기 하나 추가되었더니 빙고가 2개 늘어나서 4개가 된다거나 할 수 있음.
                print(bingo_call.index(judge_call_num) + 1)
                print(my_bingo)
                num_of_bingo = 0
                break
        if num_of_bingo >= 3:  # 갑자기 하나 추가되었더니 빙고가 2개 늘어나서 4개가 된다거나 할 수 있음.
            break
    if num_of_bingo >= 3:  # 갑자기 하나 추가되었더니 빙고가 2개 늘어나서 4개가 된다거나 할 수 있음.
        break

print(my_bingo)
print(my_bingo_t)