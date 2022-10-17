import sys

def test(coor_a, coor_b, coor_c):
    a_x, a_y = coor_a
    b_x, b_y = coor_b
    c_x, c_y = coor_c

    if (a_x-b_x)**2 + (a_y - b_y)**2 == (b_x-c_x)**2 + (b_y - c_y)**2 + (c_x-a_x)**2 + (c_y - a_y)**2:
        return True
    elif (b_x-c_x)**2 + (b_y - c_y)**2 == (a_x-b_x)**2 + (a_y - b_y)**2 + (c_x-a_x)**2 + (c_y - a_y)**2:
        return True
    elif (c_x-a_x)**2 + (c_y - a_y)**2 == (a_x-b_x)**2 + (a_y - b_y)**2 + (b_x-c_x)**2 + (b_y - c_y)**2:
        return True
    else:
        return False

N = int(input())
coor_list = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

# 3점을 골랐을때, set에 넣고 coor의 x좌표, y좌표를 봐서 각기 다른값 4개라면 무조건 직각 삼각형이 된다.
# 근데 그게 안되었을때 대각선을 따라서 직각 삼각형이 되는 경우.. 어쩔수없이 봐야함.. a^2 = b^2 + c^2을 3번 대입해서 통과하면 okay

cnt = 0
coor_nums = len(coor_list)
for i in range(coor_nums):
    for j in range(i+1, coor_nums):
        for k in range(j+1, coor_nums):
            small_coors = [coor_list[i][0], coor_list[i][1], coor_list[j][0], coor_list[j][1], coor_list[k][0], coor_list[k][1]]
            coor_set = set(small_coors)
            if len(coor_set) == 4:
                cnt += 1
                continue
            elif test(coor_list[i], coor_list[j], coor_list[k]):
                cnt += 1
                continue
            else:
                pass
print(cnt)



