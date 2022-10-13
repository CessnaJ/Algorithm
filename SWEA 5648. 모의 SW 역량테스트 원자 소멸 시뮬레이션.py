'''
1. 원자의 최초 위치는 2차원 평면상의 [x, y] 이다.

2. 원자는 각자 고유의 움직이는 방향을 가지고 있다. (상하좌우 4방향)

 - 상: y 가 증가하는 방향

 - 하: y 가 감소하는 방향

 - 좌: x 가 감소하는 방향

 - 우: x 가 증가하는 방향

3. 모든 원자들의 이동속도는 동일하다. 즉, 1초에 1만큼의 거리를 이동한다.

4. 모든 원자들은 최초 위치에서 동시에 이동을 시작한다.
5. 두 개 이상의 원자가 동시에 충돌 할 경우 충돌한 원자들은 모두 보유한 에너지를 방출하고 소멸된다.
'''
# 둘이 만난다는걸 어떻게 해야할까?
# 만나면 해당 대상 값 더하고 삭제해주는식으로 sequence를 짤 수 있다.



T = int(input())
# 0 1 2 3 상 하 좌 우
dx = [0, 0, -0.5, 0.5]
dy = [0.5, -0.5, 0, 0]
for case in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    # [[x위치, y 위치, 이동방향, 보유에너지], [ 동일 순서 ]... ]
    # 속도는 똑같으니까 제일 먼저 만나는 애들 삭제시키면서 에너지 합으로 넣고, 그 다음 시퀀스 반복해서 반응하는게 없으면 return 해주면 될거같다.
    sum_energy = 0
    # 소수점으로 만나는 경우도 봐야하니까 그냥 방정식 계산을 통해서 빨리 만나는애들로 우선제거 해주면 된다.
    for _ in range(4000):
        repeat = len(atoms)
        for i in range(repeat): # 1초후 좌표 갱신
            atoms[i][0] += dx[atoms[i][3]]
            atoms[i][1] += dy[atoms[i][3]]
        del_candidate = []
        for j in range(repeat):
            for k in range(j+1, repeat):
                if atoms[j][0] == atoms[k][0] and atoms[j][1] == atoms[k][1]:
                    del_candidate += [j, k]
                    sum_energy += (atoms[j][3] + atoms[k][3])

        for x in range(len(del_candidate)):

    print(f'#{case}')