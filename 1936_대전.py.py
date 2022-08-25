A, B = map(int, input().split())

if A == 3 and B == 1:
    print("B")
elif A == 1 and B == 3:
    print("A")
elif A < B:
    print("B")
else:
    print("A")
