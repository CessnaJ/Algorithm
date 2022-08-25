N = int(input())

for i in range(N):
    test_case = input()
    if test_case == test_case[::-1]:
        print(f"#{i + 1} 1")
    else:
        print(f"#{i + 1} 0")