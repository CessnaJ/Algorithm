demands = list(map(int, input().split())) + [0]
tickets = list(map(int, input().split())) + [0]
heads = 0


for i in range(3):
    heads += min(demands[i], tickets[i])
    tickets[i] -= demands[i]
    if tickets[i] > 0:
        tickets[i+1] += tickets[i]//3
print(heads)