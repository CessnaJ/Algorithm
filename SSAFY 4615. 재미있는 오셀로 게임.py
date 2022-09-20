# 덮는다고 생각했음. 좌표들. set이니까 차집합으로 없애버리면..? (만들다보니 안될거같음)
DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # 0 to 7
# up, upright, right, downright, down, downleft, left, upleft 순서

T = int(input())

def close_coor_search(direction, anchor, color):
    count = 1
    next_coor = [anchor[0] + count*direction[0], anchor[1] + count*direction[1]]
    while True:
        if board[next_coor[0]][next_coor[1]] != color:
            break
        count += 1
    return [next_coor[0], next_coor[1]]


def play_turn(new_coors, input_board):
    x = new_coors[0]
    y = new_coors[1]
    input_board[x][y] = coors[2]
    possible_list = []
    for i in range(8):
        possible_list.append(close_coor_search(DIRECTIONS[i], new_coors, coors[2]))


for case in range(1, T+1):
    board_size, turns = map(int, input().split()) # 보드 사이즈는 4,6,8 중 하나
    board = [[0]*board_size for _ in range(board_size)]
    # white_coors = {(board_size//2, board_size//2), (board_size//2 +1, board_size//2 +1)}
    # black_coors = {(board_size//2, board_size//2 + 1), (board_size//2 +1, board_size//2)}
    board[board_size//2][board_size//2] = board[(board_size//2)+1][(board_size//2)+1] = 1
    board[board_size//2][(board_size//2)+1] = board[(board_size//2)+1][board_size//2] = 2


    for _ in range(turns/2):
        new_black_coor = list(map(int, input().split()))
        play_turn(new_black_coor, board)
        new_white_coor = list(map(int, input().split()))
        play_turn(new_white_coor, board)
    print(f'#{case}')