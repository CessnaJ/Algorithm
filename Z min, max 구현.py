given_list = [1, 5, 9, 2, 4, 5, 12, 99, 35, 72, 10, 74]


# min 구현해보기
def my_min(input_list):
    minimum = input_list[0]
    for i in input_list[1:]:
        if i < minimum:
            minimum = i
    return minimum


# len 구현해보기
def my_len(input_list):
    count = 0
    for _ in input_list:
        count += 1
    return count


# max 구현해보기
def my_max(input_list):
    maximum = input_list[0]
    for i in input_list[1:]:
        if i > maximum:
            maximum = i
    return maximum


# min max 구현해보기 (min과 max를 동시에 뱉는거)
def minmax(input_list):
    minimum = input_list[0]
    maximum = input_list[0]

    for i in input_list[1:]:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i

    return [maximum, minimum]


print(minmax(given_list))
print(my_max(given_list))
print(my_min(given_list))
print(my_len(given_list))