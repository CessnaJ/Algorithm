from sys import stdin
damage = 0
max_damage = 0
rooms, myatk = map(int, stdin.readline().split())
for _ in range(rooms):
    which, attack, hp = map(int, stdin.readline().split())
    if which == 1:
        if hp % myatk: # 딱 떨어진다.
            num_of_attacked = hp // myatk
        else: # 딱 안 떨어진다.
            num_of_attacked = hp // myatk - 1
        damage += (attack * num_of_attacked)
        max_damage = max(damage, max_damage)
    else:
        myatk += attack
        damage -= hp
        if damage < 0:
            damage = 0
print(max(max_damage, damage) + 1)
