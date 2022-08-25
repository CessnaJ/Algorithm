T = int(input())

def pizza_rotation(q_array, pizza_in_ready): # 순회 큐를 이용해서 풀 수도 있겠다. 나오면 거기에 0채우고 계속 돌리는식으로.
    order = 0 # 나는 피자가 돈다고 생각하지 않고 포인터가 돈다고 생각해서 차례가 되면 방사능(치즈) 반감기가 된다고 생각하는식으로 풀것이다.
    while len(q_array) != 1: # 1개만 남을때까지 계속 돌다가 1개 남은거 뱉어낼거임.
        eliminate_idx = []
        for i in range(len(q_array)):
            q_array[i] = q_array[i]//2
            if q_array[i] == 0:
                eliminate_idx.append(i)



    return q_array[0]        # 뱉어내야지.


for case in range(1, T+1):
    oven_size, pizza_num = map(int, input().split())
    pizza_with_cheese = list(map(int, input().split()))
    pizza_in_oven = []
    for j in range(oven_size): # 기본으로 화덕 풀 충전.
        pizza_in_oven.append(pizza_with_cheese.pop(0))

    print(f'#{case}')