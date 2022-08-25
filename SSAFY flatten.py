
# 함수형으로 만들어 봤습니다. 문제풀기전에 내 생각!!
# ordered list로 만들고, max랑 min이랑 숫자 다 합쳐서 짝수면 0,
# 홀수면 1이 되게 하면 일단 될거같은데..
# 덤프 1번 할때마다 최고높이를 또 N번 search하는건 오바임.
# 아니면 counting list로 ordered 시켜서, [3 5 6 1 2 5 5 2 10 7 8 9]이런상황에서 맨끝을 평탄화시키는 방향도 있음.
# 잘못된 생각이었음. 다시 생각해서 풀어봤습니다.

'''
일단 중간에 끝나는 각인지 아닌지를 본다.
아이디어는.. dump횟수가 너무 많으면 어차피 0 아니면 1이 나오는데 그걸 굳이 다 해봐야 알까? 싶어서 그랬음.
(저 max 1000번의 노가다를 굳이 안해도 0과1은 나오는데 그걸 찾기 위함. 계산을 N번만 하면 되니까! 아마 모수가 커진다고 하면 이런식으로 한번 걸러주는게 좋다고 생각했음.)
다 합친 다음에. 평균 구해서 평균 * 개수랑 각 element의 높이차가 평탄화 횟수보다 작으면 0 아니면 1 나온다는거.
모든 element의 평균이 자연수로 떨어지면 완전평탄화가 가능하니까 0, 아니면 1.
'''
def whether_to_dump(list, total_dump_trial_num): # 위 주석에 설명 써뒀습니다.
    box_height_sum = 0 
    length_count = 0
    absolute_diff_value = 0
    for i in list:
        box_height_sum += i

    for _ in list:
        length_count += 1
    avg_height = box_height_sum/length_count
    for k in list:
        absolute_diff_value = 0
        if k > avg_height:
            absolute_diff_value += (k - avg_height)
        else:
            absolute_diff_value += -(k - avg_height)

    if total_dump_trial_num > absolute_diff_value:
        if avg_height % 1 == 0: # 평균이 정수형이라는건 딱 맞춰 떨어지는 높이가 있다는것이다. 0을 반환한다.
            return 0
        else: # 소수점으로 떨어진다는건 완전 평탄화가 불가능하다는 뜻.
            return 1
    else:
        return True



def dump(count_list): # count_list를 받아서 dump 해주는 함수.
    for idx_from_fwd in range(101):# 앞 인덱스부터 탐색 들어가서 밀어내기처럼 하나 바꿔주고, break 
        if count_list[idx_from_fwd] != 0: # 앞 인덱스부터 탐색 들어가서 밀어내기처럼 하나 바꿔주고, break 
            count_list[idx_from_fwd], count_list[idx_from_fwd + 1] = count_list[idx_from_fwd] - 1, count_list[idx_from_fwd + 1] + 1
            break

    for idx_from_bwd in range(101)[::-1]: # 앞을 하나 밀었으면 뒤도 하나 당겨와야 box를 평탄화했다고 볼 수 있음.
        if count_list[idx_from_bwd] != 0:
            count_list[idx_from_bwd], count_list[idx_from_bwd - 1] = count_list[idx_from_bwd] - 1, count_list[idx_from_bwd - 1] + 1
            break


def find_max_height_diff(count_list): # dump가 끝난 count_list를 받아서 max_height_diff를 반환해주는 함수.
    max_height = 0
    min_height = 0
    for i in range(100):
        if count_list[i] != 0:
            min_height = i + 1 # idx는 0부터. height는 1부터니까
            break
    for j in range(100)[::-1]:
        if count_list[j] != 0:
            max_height = j + 1 # idx는 0부터. height는 1부터니까 count list로 변환해서 놨기 때문에 (list의 idx가 곧 높이를 말한다)
            break
    return max_height - min_height


for case in range(10):
    N = int(input())
    given_num_list = list(map(int, input().split()))

    if whether_to_dump(given_num_list, N) == True: # 노가다를 진행할지 판단합니다.
        print(f'#{case+1} {whether_to_dump(given_num_list, N)}')
    else:
        count_list = [0]*101 # 0~100이 아니라, 1~100. 편하게 풀기 위해서 101칸을 넣어서
        for i in given_num_list: # count sort로 하나씩 채워넣었음.
            count_list[i] = count_list[i] + 1
        for _ in range(N): #dump를 N번 실행.
            dump(count_list)
        print(f'#{case+1} {find_max_height_diff(count_list)}')