A = int(input())

for i in range(A):
    B = int(input())
    string = ""
    for _ in range(B):
        X, Y = input().split()
        string = string + (X * int(Y))

    string_len = len(string)
    iterate_num = string_len//10 + 1
    print(f"#{i+1}")
    for j in range(iterate_num):
        print(string[j*10:(j+1)*10])