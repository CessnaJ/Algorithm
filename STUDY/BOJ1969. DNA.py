#생각난 방법 -> list comprehension으로 데이터를 싹 받아서 zip 처럼 치환해버리기. 첫글자 가장 공통글자 많은거 랭킹 정해서 뽑고 두번째~~~~~~n번째까지.
N, M = map(int, input().split())
list_for_zip = [input() for _ in range(N)]
hamming_distance = 0
result_DNA = ""
zipped_by_letter_order = list(zip(*list_for_zip))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in zipped_by_letter_order:
    alphabetical_count_dict = dict.fromkeys(alphabet, 0) # refresh
    max_letter = "A" # refresh
    for k in i:
        alphabetical_count_dict[k] += 1 # defalut_dict에다가 첫번째 글자들 쫙 모아봐서 카운트 시켜놓음.
    for l in alphabetical_count_dict: # default dict에 키 넣고 a부터z까지 순서대로 순회하면서 value가 이전 알파벳의 숫자를 넘겨야 바꿔주는 로직. 뱉는건 key를 뱉어서 결과값에 concatenate.
        if alphabetical_count_dict[l] > alphabetical_count_dict[max_letter]:
            max_letter = l
    result_DNA += max_letter

#max, count를 이용해서 pythonic하게 문자열의 답을 구하고, 그 다음 일일히 비교해서 hamming distance를 구할 수 있다.(근데 우리가 생각해보면 hamming distance도 한번에 구할 수 있지않나?)
# for i in zipped_by_letter_order:
#     result_DNA += max(set(i), key= i.count)
# 이렇게하면 답이 되는 DNA를 구할 수 있다.(아~ 이거 지맘대로 계산해버려서 알파벳순서로 안해주네?) dict에 키 넣고 a부터z까지 순서대로 순회하면서 이전 알파벳의 숫자를 넘겨야 바꿔주는 로직으로 넣어야하나.. 귀찮다 ㅠㅠ
for j in range(M):
    duplicated_num = zipped_by_letter_order[j].count(result_DNA[j])
    hamming_distance += (N - duplicated_num)
print(result_DNA, hamming_distance, sep='\n')

# StudentDict = dict.fromkeys(Student, None) #이걸 5번 구글에 물어봤다. 이렇게 자주쓸거면서 계속 물어보는건 지능의 문제.