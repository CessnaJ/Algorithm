num_of_customer = int(input())

tips_before_queue = [int(input()) for _ in range(num_of_customer)] # 최대치를 받기 위해서는 가장 덜줄놈을 맨 뒤로 빼서 0로 만들면 된다. 나머지는 알아서 계산된다.
# N명이라고 치면 어차피 '받은등수 -1'이니까 1등은 안깎이고, 2등은 1깎이고.. 이런식이니까
# 0이 되는 애들까지 싹 제외를 시킨다음에 (0 ~ 음수) ordered list에서 idx로 접근을 해서 계산치가 0 이하면 날리고, 아니면 tips_left 라는 list에 넣어보자.
# 남은 사람들 M명 계산을 할건데 시작을 0부터 1씩 증가하는 등차수열로 해서 가우스공식 쓰면 된다. 그만큼 tip을 빼주고, 다시 M만큼 더해주면 된다.
# 그게 더 귀찮겠다.
tips_before_subtract = sorted(tips_before_queue, reverse=True)
total_tips = 0
for i in range(num_of_customer):
    tip_after_queue = tips_before_subtract[i] -i # 이미 idx에는 1이 빠져있다.
    if tip_after_queue > 0:
        total_tips += tip_after_queue
    else:
        break # 한번 돈을 못받기 시작하면 그 뒤는 팁 안주는 쓰레기들이니까 거르자.
print(total_tips)