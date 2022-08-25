# trigger함수 만들어서 4 3 3 2 2 1 1 이런식으로 줄어드는식으로 만들어보기
# snail_marker 함수 만들어서 숫자 하나씩 마킹해나가기.
N = snail_size = int(input('Type the size of snail: '))
steps = N
whether_turn = 1
number = 1
def trigger(steps=N, whether_turn=1):
    steps = N
    repeat = 1
    if repeat == 0:
        turn()
        repeat = 2
    if steps == 0:
        repeat -= 1


    whether_turn -= 1
    #turn이 0 되면 왼쪽 90%로 회전하는걸로.

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def snail_marker(snail_size, row=0, col=0 number=1):
    snail[row][col] = number
    number += 1

def turn(row, col):
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

snail = [[0]*N for _ in range(N)]
row = 0
col = 0

for i in range(N**2):
    snail_marker(N):