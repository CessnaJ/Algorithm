#default dict를 만들고,
# list안에 list를 만들어서 비교하는 작업을 n번하면 되는거 아닌가?
# 이거 비교하는 로직넣어서 매번 event마다 순서 만들어주는 방식 + 역 stack 이용하면 됨. 꼴지 list[-1]가 replace되는걸로. 그러니까 재할당을 당한다는거임. 나간애는 0으로 카운트 다시 된다는거 보니..
default_student_vote_corresponding_list = [[i, 1] for i in range(1, 101)]
candidate = []

# 아.. candidate 개수 3개 fix가 아니구나.. 다시....... 암튼 오더 맞춰주는 로직 (아... 이게 brute force..? 하... 그래서.... 난이도 높았구나...)
def find_candidate_order(list):



    # a, b, c = list[0][1], list[1][1], list[2][1]
    # if b > a and b > c:
    #     list[0], list[1] = list[1], list[0]
    # elif a > c > b:
    #     list[1], list[2] = list[2], list[1]
    # elif c > a and c > b:
    #     list[0], list[1], list[2] = list[2], list[0], list[1]
    # else:
    #     pass
