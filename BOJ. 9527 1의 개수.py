'''
          0
          1
         10
         11
        100
        101
        110
        111
       1000
       1001
       1010
       1011
       1100
       1101
       1110
       1111
      10000
      10001
      10010
      10011
      10100
      10101
      10110
      10111
      11000
      11001
      11010
      11011
      11100
      11101
      11110
      11111
'''


'''
1 - 101010101010101
2 - 110011001100110011001100
3 - 111100001111000011110000
4 - 111111110000000011111111
5 - 1111111111111111
'''
# A, B를 2진법으로 봐서 A의 2진법 자리수, B의 2진법 자리수를 파악.
# A일때 패턴시작의 몇번째인지 보기.
# B일때 각자리 수 패턴 시작의 몇번인지 보기.
A, B = map(int, input().split())
scale = 0
while A > scale**2:



    scale += 1

