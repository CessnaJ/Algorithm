# from collections import deque
T = int(input())

for case in range(1, T+1):
    container_num, truck_num = map(int, input().split())
    containers = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)
    containers_arrived =[0]
    count =0
    while trucks and containers and count != truck_num:
        for i in range(len(containers)):
            if trucks[count] >= containers[i]:
                containers_arrived.append(containers.pop(i))
                trucks[count] = 0
                count += 1
                break
        else:
            count += 1


    print(f'#{case} {sum(containers_arrived)}')