# matrix looping using range and index technique.
# 행 우선순회, 열 우선순회 정방향 순회, 순방향순회, 지그재그순회 모든게 가능하다.
# maxrix를 순회한다는말은 내가 정한 규칙을 이용해서 하나씩 뽑아서 뭔가를 한다는말이다.

basic_matrix = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]



print('정상적인 순회로 처음은 가봐요.')
# 1. 정상적인 열 우선순회. col싹 돌고 다음 row 가서 col 싹 도는식
for row in range(len(basic_matrix)):
    for col in range(len(basic_matrix[0])):
        print(basic_matrix[row][col])


print('역순으로 순회해볼게요.')

# 2. 열을 역순으로 순회하는것. col을 역순으로 싹 돌고 다음 row 가서 다시 반복하는 logic
for row in range(len(basic_matrix)):
    for col in range(len(basic_matrix[0])-1, -1, -1):
        print(basic_matrix[row][col])

# 열 우선순회인데 col은 지그재그로 순회하는 방식.
print('이번에는 지그재그로 순회해볼게요.')
for row in range(len(basic_matrix)):
    if row%2:
        for col in range(len(basic_matrix[0])-1, -1, -1):
            print(basic_matrix[row][col])
    else:
        for col in range(len(basic_matrix)):
            print(basic_matrix[row][col])

# 이번에는 행렬 순서 바꿔서 순회해보자. 행 우선순회.
print('이번에는 행 우선순회. 전치랑 개념이 다른거니까 주의하자.')
for row in range(len(basic_matrix)):
    for col in range(len(basic_matrix[0])):
        print(basic_matrix[col][row])

empty_dict = dict()

if not empty_dict.get('개소리'):
    print('이거 무조건 나올걸?')