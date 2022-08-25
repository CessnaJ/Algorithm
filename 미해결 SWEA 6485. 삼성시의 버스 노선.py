T = int(input())

for case in range(1, T+1):
    N = int(input())

    bus_list = [list(map(int, input().split())) for _ in range(N)]

    num_of_bus_stop = int(input())

    bus_stop_list = [0]*5001
    for bus in bus_list:
        bus_start = bus[0]
        bus_end = bus[1]
        for i in range(bus_start, bus_end+1):
            bus_stop_list[i] += 1

    for j in range(num_of_bus_stop):
        int(input())

