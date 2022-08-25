# 문제해결방법 4시 15분 시작.
'''
남학생은 그냥 N의 배수 스위치 조건문 걸어서 T -> F  // F->T 이렇게 변환하는것으로 함.

여학생은 받은 숫자 기준으로 했을때, 재귀로 지어나가는걸로 함.
while로 해보자. -> N은 주어진거니까 무조건 바꾸고,
while whether_go_on: 으로 해서 진행할거면 TF flag 세우는걸로.
count를 세서 N +- count를 해서 0~7이내에 들면 진행하는것으로 조건 걸고,
좌우가 같은지 체크, 같으면 바꾸고(T면 F, F면 T로.) 바꿔진다면 count += 1

'''
# 남학생은 그냥 N의 배수 스위치 조건문 걸어서 T -> F


def change_switch(n):
    if n: # 켜져있으면 False로 바꾸고
        return 0
    elif not n: # 꺼져있으면 True로 바꾼다.
        return 1


num_of_switch =int(input())
switch_input = list(map(int, input().split())) # lenth는 num_of_switch 따라간다.
num_of_student = int(input())
student_gender_ref_num_list = []
for i in range(num_of_student):
    student_gender_ref_num_list.append(list(map(int, input().split())))

for j in student_gender_ref_num_list:
    if j[0] == 1: # 남자라면~
        for k in range(1, (num_of_switch//j[1]) + 1): # 순회해서
            switch_input[(j[1] * k)-1] = change_switch(switch_input[(j[1] * k)-1]) # 바꾼다.
    elif j[0] == 2: # 여자라면~
        start_idx = j[1]-1
        switch_input[start_idx] = change_switch(switch_input[start_idx]) # 첫 idx는 무조건 스위치 바뀌니까
        whether_go_on = True
        count = 1
        while whether_go_on: # 이제 진행이 가능한지, 양옆 idx가 같은지를 봐야한다.
            if start_idx - count >= 0 and start_idx + count <= num_of_switch-1: #start idx 기준으로 계산한게 switch list idx 범위 안인지 먼저 체크.
                if switch_input[start_idx + count] == switch_input[start_idx - count]: # 다른 범주의 조건이기 때문에 가독성 위해 세로로 나눠서 배치. 양 옆의 value가 같은지 체크
                    switch_input[start_idx + count] = change_switch(switch_input[start_idx + count])
                    switch_input[start_idx - count] = change_switch(switch_input[start_idx - count])
                else:
                    whether_go_on = False
            else:
                whether_go_on = False
            count += 1

for a in range(num_of_switch):
    if a != 0 and a % 20 == 0:
        print(end='\n')
    print(switch_input[a], sep='', end=' ')
print(end='\n')

# 내 문제점 2개 발견.
# 입출력 문법에 대한 완전한 이해가 없었음. (그리고 조건 걸거면 edge case로 0이 어떻게 될건지도 생각해봐야함. 조건문 순서도 재조정)
# 함수를 통해서 아예 밖의 값을 바꿔버리려면 name scoping을 제대로 써야했는데 구조를 다시 바꾸거나, 아예 리스트를 복사해서 재귀적으로 해결하는 방법도 있었겠지만 못해서 결국 원시적으로 해결.
