T = int(input())
scores = []
for case in range(1, T+1):
    a, d, g = map(int, input().split())
    score = a * (d + g)
    if a == (d+g):
        score *= 2
    scores.append(score)

print(max(scores))


