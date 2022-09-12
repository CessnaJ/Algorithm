total_visits = int(input())
life_consumes = list(map(int, input().split()))
joy_gains = list(map(int, input().split()))
life_joy_list = list(zip(life_consumes, joy_gains))

print(life_joy_list)
# 인사를 해서 0이하가 되는 순간 그 joy는 반영이 안된다.
# 누적 0 이상으로 맞춰놔야함.

# 효율성 순으로 정렬하고, 같을시, 덩어리 작은 순서로. 그리고 life가 100이면 맨 뒤로 뺀다.
sorted_life_joy = sorted(life_joy_list, key=lambda x: x[0]/x[1])
print(sorted_life_joy)

