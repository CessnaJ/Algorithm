# 10개의 정수를 입력받아, 부분집합의 합이 0이 되는게 존재하는지 계산하는 함수를 작성.

# 1111111111 ~ 0000000000
# 풀기 전 생각. 가능한 bit의 조합을 싹 출력해서 그걸 iterable로 돌려서 1/0 곱한다음에 그걸 넣은 list의 객체를 합하면 되는거 아닌가? 여부는 flag 만들어서 출력해버리고.
T = int(input()) # test case 개수
N = 10           # 문제에서 input 개수를 10개로 통일했네요?
for case in range(1, T+1): # test case만큼 돌릴거구요, print에 양식맞춰서 print 해줄겁니다.
    given_list = list(map(int, input().split())) # input list로 받을겁니다. 함수는 여기서만. 아.. binary문자열로 바꿔서 한번 해보고 싶었어요.

    for i in range(1<<N): # 오늘 배운 bit연산자 이용해서 2^N을 만들어줍니다. N개의 원소를 가진 set의 subset 개수는 2^N개 입니다. 공집합 포함.
        subset = []
        sum_of_subset = 0
        whether_0_exist = 0
        idx = 0
        binary_trans = bin(2**N + i) # binary 000001 이런식이어도 자리수 안없어지게 2의 N승 더해봤습니다.
        for TF in binary_trans[3:]: # 0b100000001 이렇게 만들고 for loop은 3번째 자리부터 해줄거에요.
            if int(TF) == 1:
                subset += [given_list[idx]]
            idx += 1
        else:
            idx = 0

        for element in subset:
            sum_of_subset += element
        if sum_of_subset == 0 and subset != []: # 공집합을 없애야하는구나 아...... 뒤 조건 안붙히면 무조건 0 나오긴하지.. 이런식이면
            whether_0_exist = 1
            idx = 0
            break
    print(f'#{case} {whether_0_exist}')
