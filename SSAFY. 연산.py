from collections import deque

T = int(input())

for case in range(1, T+1):
    start, result = map(int, input().split())
    calc_set = set()
    calc_set.add(start)
    queue = deque()
    queue.append(start)
    count = 0
    while result not in calc_set:
        for _ in range(len(queue)):
            current = queue.popleft()
            if current+1 not in calc_set and 1 <= current+1 <= 1000000:
                calc_set.add(current+1)
                queue.append(current+1)
            if current-1 not in calc_set and 1 <= current-1 <= 1000000:
                calc_set.add(current-1)
                queue.append(current-1)
            if current*2 not in calc_set and 1 <= current*2 <= 1000000:
                calc_set.add(current*2)
                queue.append(current*2)
            if current-10 not in calc_set and 1 <= current-10 <= 1000000:
                calc_set.add(current-10)
                queue.append(current-10)
        count += 1

    print(f'#{case} {count}')

