# ()가 바로 붙어있으면 레이저고, 아니면 쇠막대로 치는것.
# ()(((()())(())()))(())

# 해당 막대 안에 레이저가 몇개 있는지 n개를 세고 그 다음에 N+1개로 박살난다고 보면 됨. -> 이렇게 하면 스택으로 푸는게 아님.
#
#
# 이 문제는 컴퓨터가 코드를 어떻게 읽어나가지는지를 생각하면서 풀면 된다.
# 직관적으로 봤을때, 그냥 한번에 쫙 쏴서 개수를 구하고 싶지만, 컴퓨터는 한번에 한가지 일밖에 할 수 없다.
# 그리고 컴퓨터가 코드는 좌측에서 우측으로 1개씩 읽어나간다.
# 이걸 내가 여러 layer로 담아줄게 아니면, 코드를 읽어가나는 특성을 이용해줘야한다. 맨위에 한번에 쫙 해준다는걸 구현하면 layer가 여러개 생길거다.
#
# 그래서 레이저를 한번 쏘면, 왼쪽 조각들이 모일것이고, 그림이 리셋된다고 보면 됨.

class Stack: # stack이라는 class를 만들어봅니다. 사실 이거 이렇게 안풀어도 되는데, 한번도 안짜봐서 경험삼아서 만들어봤습니다.
    def __init__(self):
        self.box = []
        self.pipe_pieces = 0

    def push(self, item):
        self.box.append(item)

    def pop(self):
        return self.box.pop()  # stack 끝을 제거하면서 return 해준다는거. LIFO

    def top(self):
        return self.box[-1]

    def size(self):
        return len(self.box)


pipe_n_laser = Stack()
given_data = input()
pipe_pieces = 0
for i in range(len(given_data)): #str형인 괄호가 한글자씩 들어가면서 stack에 무슨 일이 일어날것이다.
    if given_data[i] == '(':
        pipe_n_laser.push(given_data[i]) # '('이거면 일단 무조건 넣는다.
    else: # 닫는 괄호일때,
          # 닫는 괄호라면 레이저인지를 먼저 본다. 레이저라면 일단 pop하고 stack 개수 세주면 파이프개수가 된다. 직전 stack을 확인하고 닫혀서 pop이 되어도, 만약에 그게 레이저로 잘린게 아니라 파이프의 끝이라면, 1만 더해준다.
        if given_data[i] != given_data[i-1]: # 같지 않다는 말이 () 이렇게 바로 한쌍이라는말이다. 근데 이거는 str로 받은 given data를 보는 조건임. #stack 내에서 비교하는게 아니다.
            pipe_n_laser.pop()
            pipe_pieces += pipe_n_laser.size() # 살아있는 파이프 개수를 싹 더해줌.

        else: # 이거는 )) 이렇게 겹치는걸 말하는건데, 이러면 하나 더해주면서 stack을 pop으로 없애준다.
            pipe_pieces += 1
            pipe_n_laser.pop()
print(pipe_pieces)
# 한마디로 말해서 laser면 n개를 더해주고, laser가 아니라면 1개를 더해준다!