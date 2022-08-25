# triplet을 구하기 위해서 set을 넣은 다음에 원소 몇개인지 세면 되네? 원소 4개면 (아 이건 2개,2개인 경우에도 포함임. GG)
# count sort이용해서 풀어보자. 0이 1개! 0이 2개! 이런식으로 쭉 가서 먼저 제거하는게 triplet. 어차피 triple 1개 있으면 그 다음에는 [i:i+2]이렇게 해서 111이 있는지 확인하면 됨.
# 만약에 triplet이 없다고 하면, 연속 3개 index에 -1씩을 해보고, list에서 -1 or -2인게 안뜨면, 그부분이 연속 3개가 양수였다는거니까. 2중 for loop으로 가능하다.
# 카드가 4 set니까 triple은 1개만 존재가능.
#
# test = [1, 2, 3, 4, 5]
# print(test[2:4])


# import random
# input_list = []
# for i in range(6):
#     input_list.append(random.randint(0, 9)) # input이 안주어지니.. 이건 함수 쓴거 아닙니다!
input_list = [2, 3, 4, 6, 7, 8]

count_list = [0] * 12 # 0이 12개인 default_list를 생성합니다.(index error방지 뒤에 2개 더 끼워넣습니다.)
for j in input_list:
    count_list[j] += 1 # 이렇게 해서 0~9까지 몇개씩 들어있는지 count_list를 만들 수 있습니다.

for m in range(10):
    if count_list[m] == 3 or 4: # triple이 1개 주어져서 run 1개만 찾으면 되는 경우.
        count_list[m] = count_list[m] - 3
        for n in range(8): # 3이나 4가 1개 있어서 그 숫자에 3 빼고 1이 연속으로 3개 있는걸 탐색하는 경우!
            if count_list[n:n + 3] == [1, 1, 1]:
                print('I got baby_gin!!')
            elif 3 in count_list: # 3을 뺐는데 3이 또 있는 경우. 3이 2개!
                print('I got baby_gin!!')
        count_list[m] += 3 # 다시 더해줘야 refresh 된 상태로 다음 for loop을 돌릴 수 있다.
    else: #run을 2개 찾아야하는 경우
        for a in range(8):
            if count_list[a:a + 3] == [1, 1, 2] and count_list[a + 2:a + 5] == [2, 1, 1]: # 부분 중첩되면 연속되서 1이 나와야함.
                print('I got baby_gin!!') # 왼쪽에서 순회가 돌아가기때문에 211이나, 121은 나와봤자 쓸모가 없다. 오히려 continue 해줘야하는 경우.
            elif count_list[a:a + 3] == [1, 2, 2] and count_list[a + 1:a + 4] == [2, 2, 1]: # 부분 중첩되면 연속되서 1이 나와야하니.
                print('I got baby_gin!!')
            elif count_list[a:a + 3] == [2, 2, 2]: # 1,1,1이 2겹으로 완전 중첩
                print('I got baby_gin!!')
            elif count_list[a:a + 3] == [1, 1, 1]: # 1,1,1을 발견한 후 그 우측 list에서 1,1,1이 또 있는경우!
                for b in range(a+3, 8):
                    if count_list[b: b + 3] == [1, 1, 1]:
                        print('I got baby_gin!!')
            else:
                pass

#
#
#
#                     or [1,2,2] or [2,2,2]:  # 왼쪽에서 순회가 돌아가기때문에 211이나, 121은 나와봤자 쓸모가 없다.
#
#
#
#                 if input_list[a+2: a+5] == [2,1,1] and a < 3:
#                     print('I got baby_gin')
#             elif input_list[a:a+3] == [1,1,1]:
#
#
#
#
# if 3 or 4 in count_list: # triple이 일단 1개 나온 경우 (run만 1개 뜨면 됨.)
#     for n in range(0,8):
#         input_list[n:n + 3]
#
#
# else: #triple이 안나온경우.
#
#
# for k in range(0, 8): #k idx 기준으로 +2까지 진행할거라서 idx error안나게 세팅합니다.
#     if -1 or -2 not in input_list[k:k+3]:
#
# # 00000000000
# # 30001110000
# # 01410000000
# # 00000011400
# # 00100101111
# # 12111000000
# # 00211200000
# # 00212100000
# given = [1,2,3,4,5]
#
# given[1:3] = [1,1,1]
# print(given)
