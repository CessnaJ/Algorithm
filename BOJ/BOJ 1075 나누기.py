N = input()
F = input()

change = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'] + list(map(str, range(10, 100)))

for last_two_digit in change:
    if int(N[:-2] + last_two_digit) % int(F) == 0:
        print(last_two_digit)
        break
