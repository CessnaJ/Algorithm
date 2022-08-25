'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

N이 종점 숫자인데 station 개수는 0~N. N+1개
K 배터리 용량
M 충전기 개수
list로 충전기 있는 위치를 친절하게 알려줌.

최대한 뻗어보고 그 위치에 스테이션 없으면 1칸씩 뒤로 가면서 station이 있는 위치를 파악하고, 거기서 배터리 충전을 하는 logic. 그리고 직전위치까지 순회했는데 충전기가 없으면 (for-else사용) 굳이 그 다음 볼 필요 없으니 break써서 0 출력.
'''

T = int(input())
for case in range(1, T+1):
    K, N, M = map(int, input().split())
    charger_location_list = list(map(int, input().split()))
    charger_simulation = [0] * (N+1)
    for i in charger_location_list:
        charger_simulation[i] = 1 # idx 써서 farthest station 구하기 위함.

    distance_to_destination = N
    remaining_battery = K
    num_of_remaining_charger = M
    min_num_of_charge = 0

    current_location = 0
    farthest_station_within_battery = 0

    while distance_to_destination > 0:
        max_location_for_now = current_location + remaining_battery
        max_location_to_farthest_station = 0
        for j in charger_simulation[max_location_for_now: current_location: -1]: #charger_simul에 나온 좌표에서 역순으로 탐색해서 가장 먼 station의 idx를 찾습니다.
            if distance_to_destination - (current_location + K) <= 0:
                distance_to_destination = False
                break
            if j == 1:
                farthest_station_within_battery = max_location_for_now - max_location_to_farthest_station
                min_num_of_charge += 1 # 역순 loop돌리면서 한계에서 가장 가까운 station 발견하면 전기 넣음.
                current_location = farthest_station_within_battery # 어차피 포인터 찍는거라서 복잡도에 영향없으니 가독성을 위해 변수 이름 2개가 같은 값을 가지는걸로 했습니다.
                break
            else:
                max_location_to_farthest_station += 1
        else:
            distance_to_destination = False # 더이상 볼 필요가 없다는 의미로 falsy로 해석되게 넣습니다.
            min_num_of_charge = 0

    print(f'#{case} {min_num_of_charge}')



#최대한 뻗을거니까.. 충전! 시키고 최대한 갈 수 있는곳까지의 charger까지 감. 그리고 그 직전에서 charge 하는걸로. 그리고 그게 안통하면 더이상 계산 할 필요 없지. 0넣고 break.