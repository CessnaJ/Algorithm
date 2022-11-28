demands = list(map(int, input().split())) + [0]
tickets = list(map(int, input().split())) + [0]
heads = 0

i = 0
for i in range(4):
    heads += min(demands[i], tickets[i])
    if tickets[i] - demands[i] < 0:
        tickets[i] = 0
        demands[i] = abs(tickets[i] - demands[i])
    else:
        heads += (tickets[i] - demands[i])
        tickets[i] = tickets[i] - demands[i]
        tickets[i+1] += tickets[i]//3
    i %= 3

print(heads)