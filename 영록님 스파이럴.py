def spiral(N, clockwise):
    field = [[1 for i in range(N)] for i in range(N)]
    num = N-1
    count = 0
    start = 0
    half = (N-1)//2
    while True:
        if num == 0 or num == 1:
            if num == 0:
                field[half][half] = start+1
            else:
                field[half][half] = field[half][half+1] = field[half +
                                                                1][half] = field[half+1][half+1] = start+1
            break
        for j in range(num):
            field[count][j+count] = field[j+count][N-1-count] = field[N -
                                                                      1-j-count][count] = field[N-1-count][N-1-j-count] = j+1+start

        start = field[count][N-2-count]
        num -= 2
        count += 1
    if not clockwise:
        field = field[::-1]
    return field

print(*spiral(10, True), sep="\n")
