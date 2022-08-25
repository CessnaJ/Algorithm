# '''
# 어떻게 문제를 풀까?
# bitmask 이용해서 하나씩 대입한다. 부분집합개수 맞춰서 만들어보자!
# 그리고 sum 이용해서 합이 맞는지, 개수는 맞는지? try it!
#
# '''
# T = input()
# N, K = map(int, input().split()) # N 부분집합 원소의 수. K 원하는 부분집합의 원소합.
# elements_num_of_subset = N # 보기 싫어서 줄글로 치환합니다.
# sum_of_subset = K # 얘도 치환. 포인터 한번 찍는거니까 계산수에 영향없습니다.
# num_of_elements = 12 # 문제에서 통일해줬네요. 재사용성 위해 변수로 만들어줍니다.
# given_list = list(range(1,num_of_elements+1))
#
# def find_matching_subset_num(elements_num_of_subset, sum_of_subset):
#     for i in range(1<< num_of_elements): #부분집합 개수만큼 반복
#
#
#
# for case in range(1, T+1):
#
#
#     print(f'#{case} {ans}')
#
#
#
# # bitmask돌려서 개수 3개 아니면 break하는거.
# for j in range(1<<len(given_list)):
#     if i & (1<<j): #이 상위에 있는 모든 부분집합 대입하는 for loop(bitmask)와 대입해서 1의 개수 카운트. 3이 안되면 볼 것 없으니 count리셋하고 break해서 로직 깨부심. 아니면 count만 0으로 리셋하고 다음 진행.
#         count +=1
# else:
#     if count != 3:
#         count = 0
#         break
#     else:
#         count =0
'''
오늘도 내가 나를 고생시킨다. 처음부터 다시!
함수형 프로그래밍을 한다고 해서 모든걸 함수로 만들어서 조립한다고 생각할 필요 없다.
top-down으로 동시에 2~3개의 함수를 만들어보려고 하니까 힘든거다. 조금만 복잡해져도 name scaping에서 문제가 생길것.
적당히 반대방향으로도 섞어서 진행해야함.
결국 본질은 문제해결인거고, 그 중에 재사용성, 가독성, 추상화를 위해서 함수형 프로그래밍을 하는 것.
문제를 잘게 쪼개서 컴퓨터가 이해할 수 있는 로직으로 설계하고, 그 모아주는게 더 효율적인 단계들을 모아서 함수를 만들면 된다!
'''

'''
문제에서는 무엇을 원하나? => 1~12 원소로가진 집합A // 부분집합중 원소개수 N개, N개 element들의 합이 K인게 몇개인지? 없으면 0 출력.

만들기 전 계획. 문제해결 어떻게 할까?
subset을 bitmask로 순회해서 한번본다. 
list에 넣기전에, 부분집합의 개수가 3개가 아니라면(bitmask 순회 합이 3이 아니라면) break/continue 통해서 그 회차 건너 뜀.
이 방식을 통해서 계산수를 줄일 수 있다. 
그렇게 모인 친구들의 sum 비교해보고 넣는다.
오늘까지만 내장함수 안쓴다. 내일부터는 다 쓰고 살자.
'''




# T = int(input())
# for case in range(1, T+1):
#     N, K = map(int, input().split()) # N 부분집합 원소의 수. K 원하는 부분집합의 원소합.
#     target_elements_num_of_subset = N # 보기 싫어서 줄글로 치환합니다.
#     target_sum_of_subset = K # 얘도 치환. 포인터 한번 찍는거니까 계산수에 영향없습니다.
#     num_of_elements = 12 # 문제에서 통일해줬네요. 재사용성 위해 변수로 만들어줍니다.
#     given_list = list(range(1, num_of_elements+1))
#
#     target_sum_matching = 0
#     subset_list = []
#     for i in range(1 << (len(given_list)+1)): # 0~ 2^list_length -1 for loop.
#         existence_count = 0
#         idx = 0
#         subset = []
#
#         sum_of_subset = 0
#         convertedtobin = bin(i)[3:]
#         for existence in bin(i)[3:]:
#             if existence == '1':
#                 existence_count += 1
#                 subset += [given_list[idx]]
#             idx += 1
#         if existence_count != target_elements_num_of_subset:
#             continue
#         else:
#             if subset in subset_list:
#                 continue
#             else:
#                 subset_list.append(subset)
#
#
#         for element in subset:
#             sum_of_subset += element
#         if target_sum_of_subset == sum_of_subset:
#             target_sum_matching += 1
#
#     print(f'#{case} {target_sum_matching}')


T = int(input())
for case in range(1, T+1):
    N, K = map(int, input().split()) # N 부분집합 원소의 수. K 원하는 부분집합의 원소합.
    target_elements_num_of_subset = N # 보기 싫어서 줄글로 치환합니다.
    target_sum_of_subset = K # 얘도 치환. 포인터 한번 찍는거니까 계산수에 영향없습니다.
    num_of_elements = 12 # 문제에서 통일해줬네요. 재사용성 위해 변수로 만들어줍니다.
    given_list = list(range(1, num_of_elements+1))

    target_sum_matching = 0
    subset_list = []
    for i in range(1 << (len(given_list)), 1 << (len(given_list)+1)): # (2^list_length) -1~ (2^(list_length+1)) -1 for loop.
        existence_count = 0
        idx = 0
        subset = []   # 다른 사람들이 안했을법한 방법으로 하다 보니까 버그가 생겼습니다. 그거 잡는다고 이상한 짓..

        sum_of_subset = 0
        convertedtobin = bin(i)[3:] # 0b1xxxxx 이런식으로 나올거니까
        for existence in bin(i)[3:]:
            if existence == '1':
                existence_count += 1
                subset += [given_list[idx]]
            idx += 1
        if existence_count != target_elements_num_of_subset:
            continue
        else:
            if subset in subset_list: # 문자열로 비교하다보니까 111 이랑 11100 111000이 모두 같은 결과를 뽑았습니다. 괜히 최적화가 필요해졌습니다.
                continue
            else:
                subset_list.append(subset)


        for element in subset:
            sum_of_subset += element
        if target_sum_of_subset == sum_of_subset:
            target_sum_matching += 1

    print(f'#{case} {target_sum_matching}')














