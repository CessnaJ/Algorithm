# N - 총 학생의 수
# K - 졸고 있는 학생의 수
# Q - 출석코드 보낼 학생 수
# M - 주어질 구간의 수

# 공배수
# 다 구현할 필요 없음. range에 있는것만 보는게 낫지?
# 제거해나가는게 나을까? 추가해나가는게 나을까?

total_student, doze_num, total_trial, range_num = map(int, input().split())

attendance = [False]*(total_student+3) # 0, 1, 2를 버린다.
doze_list = list(map(int, input().split()))
trial_list = list(map(int, input().split()))

range_list = [list(map(int, input().split())) for _ in range(range_num)]
# [start, end]로 묶임
# start, end = map(int, input().split())
answer_set = set()
count = 0
for _ in range(range_num):
    start, end = map(int, input().split())

    for num in range(start, end+1):
