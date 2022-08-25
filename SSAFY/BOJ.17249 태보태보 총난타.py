taebo = input()

left_right = taebo.split('(^0^)')
for i in left_right:
    print(i.count('@'), end=" ")
