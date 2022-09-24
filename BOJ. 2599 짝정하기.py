# 일단 기본 생각. -> 남자가 쏘고 여자가 받는다.
# a남자가 두 집단으로 나뉘어져서   b,c로 감
# b남자가 두 집단으로 나뉘어져서 a,b  로 감
# c남자가 두 집단으로 나뉘어져서 a, ,c로 감
# a 두조각이 합쳐져서 a여자숫자랑 같으면 짝이 맞는거임.
# b 두조각이 합쳐져서 b여자숫자랑 같으면 짝이 맞는거임.
# c 두조각이 합쳐져서 c여자숫자랑 같으면 짝이 맞는거임.


def backtracking(boy_division, school):
    if boy_division > original_students[school][1]:
        return True
# backtracking할때, break는 점점 더 커지는 애니까 뒤에꺼 볼것 없다는 뜻.
# continue는 점점 더 작아지는 애니까 다음회차를 보자는 뜻.


N = int(input())
original_students = []
for _ in range(3):
    original_students.append(list(map(int, input().split()))) #[[a남,a녀], [b남,b녀], [c남,c녀]]

for_test = [original_students[0][1], original_students[1][1], original_students[2][1]]
matching_candidate = [[0,0],[0,0],[0,0]]
done = 0
for i in range(original_students[0][0]+1): # 매칭을 0부터 a반 남학생 숫자까지 함.(b반 여자애들이랑)
    matching_candidate[0][0] = i # a남자 -> b여자
    if backtracking(i, 1):
        break
    matching_candidate[0][1] = x = original_students[0][0] - i # a남자 -> c여자
    if backtracking(x, 2):
        continue
    for j in range(original_students[1][0]+1):
        matching_candidate[1][0] = j # b남자 -> a여자
        if backtracking(j, 0):
            break
        matching_candidate[1][1] = y = original_students[1][0] - j # b남자 ->c여자
        if backtracking(y, 2):
            continue
        for k in range(original_students[2][0]+1):
            matching_candidate[2][0] = k # c남자 -> a여자
            if backtracking(k, 0):
                break
            matching_candidate[2][1] = z = original_students[2][0] - k # c남자 -> b여자
            if backtracking(z, 1):
                continue
            if [j+k, i+z, x+y] == for_test:
                done = 1
                print(done)
                print(*matching_candidate[0], sep=' ')
                print(*matching_candidate[1])
                print(*matching_candidate[2])
                break
        if done:
            break
    if done:
        break

# if original_students == matching_candidate:
#     print(i,j, )