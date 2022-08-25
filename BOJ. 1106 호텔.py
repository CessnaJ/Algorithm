# 첫줄에 target 홍보해야하는 사람들 숫자 C, 홍보할 수 있는 도시 숫자 N 주어짐
# 이 문제는 비용별 단위숫자를 계산 한다음에 그걸로 최대한 채우고(단위돈으로 단위인원을.),
# 자연수배가 되는걸로 프로그램을 짜면 될거같다.
# 만약에 안맞으면 1개 빼고, 나머지 숫자들 더해서 해가 나올 수 있는지 bruteforce로 진행해본다.
# 계속 진행. 아마 단위비용이 작은 순서로 일단 list를 나누고, 1번으로 최대한 채운 뒤, 부족한지 확인하는걸로 갈듯.

target_people, row_input = map(int, input().split())
invest_customer_increase_list = []
for i in range(row_input):
    invest_customer_increase_list.append(list(map(int, input().split())))

def bubble_sort_by_unit_cost(given_list):
    for i in range(len(given_list)-1, -1, -1): #단위 돈당 효과가 더 큰걸로 정렬을 시키겠다.
        for j in range(i):
            if given_list[j][1]/given_list[j][0]<given_list[j+1][1]/given_list[j+1][0]:
                given_list[j], given_list[j+1] = given_list[j+1], given_list[j]
    return  invest_customer_increase_list

print(bubble_sort_by_unit_cost(invest_customer_increase_list))

unit_person_list = []
for unit in invest_customer_increase_list:
    unit_person_list.append(unit[1])
print(unit_person_list)

money_count = 0
person_left = target_people +0
# 그다음 어떻게 할까? 가장 효율좋은놈으로 꽉채워. 그래서 person_left가 -가 되면 다시 하나 빼고 다음놈으로 꽉 채워., 그게 안되면 하나빼고 다시 다음놈으로
# 반복하다가 만약에 두번째놈을 안쓰는게 낫다는게 나오면 세번째놈부터 꽉 채우고 ~~~~ 반복.
while person_left: #0이 될때까지 계속 돌아간다.
    pass # 어떻게 해야할지 알지?
