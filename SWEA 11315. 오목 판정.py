T = int(input())

def diagonal_recursive(start_row, start_col, direction=True, count=0): # 대각선으로 타고가서 5개 되면 true를 반환.
    if direction:
        if board[start_row][start_col] == 'o':
            count += 1
            if count == 5:
                return True
        else:
            count = 0
        if 0 <= (start_row + 1) < board_size and 0 <= (start_col + 1) < board_size:
            return diagonal_recursive(start_row + 1, start_col + 1, True, count)

    else:
        if board[start_row][start_col] == 'o':
            count += 1
            if count == 5:
                return True
        else:
            count = 0
        if 0 <= (start_row + 1) < board_size and 0 <= start_col - 1 < board_size:
            return diagonal_recursive(start_row + 1, start_col - 1, False, count)




def perpendicular_search():
    for row in range(board_size):
        if 'ooooo' in board[row]:
            return True

    for col in range(board_size):
        count_c = 0
        for row in range(board_size):
            if board[row][col] == 'o':
                count_c += 1
                if count_c == 5:
                    return True
            else:
                count_c = 0


for case in range(1, T+1):
    board_size = int(input())
    board = [input() for _ in range(board_size)]

    if perpendicular_search():
        print(f'#{case} YES')
        continue

    for i in range(board_size):
        if diagonal_recursive(0, i, True) or diagonal_recursive(0, i, False) or diagonal_recursive(i, 0, True) or diagonal_recursive(i, 0, False) or diagonal_recursive(i, board_size - 1, False):
            print(f'#{case} YES')
            break
    else:
        print(f'#{case} NO')






    # exist = False
    # for row in range(board_size):
    #     if 'ooooo' in board[row]:
    #         exist = True
    #
    # for col in range(board_size):
    #     for row in range(board_size):
    #         exist = False
    #         count = 0
    #         if board[row][col] == 'o':
    #             count +=1
    #             if count == 5:
    #



