# 풀기 전 생각! 우리는 진법 변환을 어떻게 하는가?
# x라는 숫자를 a진법으로 변환하기 위해서 x를 a로 안나눠질때까지 계속 나누는 과정을 반복하게 된다.
# 마지막으로 몫이 a 미만으로 나왔을때, 역순으로 싹 더한게 진법 변환수가 되는것. 이걸 이용해서 몇진법인지 역산이 가능하다.

# dictionary를 이용해서 default dict를 연결해서 chain으로 만들면 쉽게 시각화를 시킬 수 있을것이다. 0~9까지숫자. a부터 10~ z가 35로 매칭되니까
conversion_key = '0123456789abcdefghijklmnopqrstuvwxyz' # 기본 dict를 만들어서 쉽게 매칭.
conversion_dict = dict.fromkeys(conversion_key)
number = 0
for i in conversion_dict:
    conversion_dict[i] = number
    number = number + 1
# 예시에서 나온 ep와 jh이 같아야한다.
# ep == jh 가 되려면 x진법 y진법으로 나뉘어야함. 표기법 자체는 max36진법으로 표기된걸로 끊어지지만 어디서 올려서 제곱시킬지는 다름.
# 방정식으로 만들어서 서로 나눈 값이 1이 되는 x,y를 찾아내고(어차피 진법이 max 36진법이라서 brute force돌리면 해결될정도의 작은 수이다.)
# 매칭이 되면 그 쌍을 list속에 넣어줄것이다. matching되는게 2개 이상이면 멀티플 출력, 0개면 impossible 출력

matching_list = []
example = input().split()
a_before_conv = example[0]
b_before_conv = example[1]
from_this_a = 0
from_this_b = 0
for i in a_before_conv:
    if conversion_dict[i] > from_this_a:
        from_this_a = conversion_dict[i]

for j in b_before_conv:
    if conversion_dict[j] > from_this_b:
        from_this_b = conversion_dict[j]


# brute force 숫자를 줄이기 위해서 각 input에서 나오는 max 글자 이상의 진법만 test한다. (예를 들어서 z가 써있는데 2진법일 수는 없는것. z라는게 20진법에 있을 수 없는 숫자다.)


for x in range(from_this_a, 36):     # 진법 갈겨보기
    for y in range(from_this_b, 36): # 서로 다른 숫자로 대응해봐야 매칭을 판단 가능하니 이렇게.
        if x != y:
            temp_a = 0
            temp_b = 0
            scale_a = 0
            scale_b = 0
            for digit in a_before_conv[::-1]: # 맨 뒷자리부터 해당 진법 단위로 scale up하면서 자리수 더해가는 식으로 계산해나갈것이다.
                temp_a += (conversion_dict[digit] * (x ** scale_a)) # x^0은 1이니까.
                scale_a += 1
            for digit in b_before_conv[::-1]:
                temp_b += (conversion_dict[digit] * (y ** scale_b))
                scale_b += 1

            if temp_a == temp_b:
                matching_list.append([temp_a, x, y])

# 다 돌렸으니까 뽑자.
if not len(matching_list):
    print('Impossible')
elif len(matching_list) > 1:
    print('Multiple')
else:
    print(*matching_list[0])
