# 어떻게 풀것인가? 1자리씩 1/2^n 으로 진행해나가면서 13번째 계산할 차례가 되면 overflow를 출력하는식. 그 전에 딱 떨어지면 그냥 answer를 출력한다.
# N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.

def float_to_bin(target):
    count = 1            # 1부터 overflow 판별여부, 2진법 소수의 자리수를 의미 (누적합의 재료가 되는 addible과 연동)
    calculating = 0       # 누적합을 통해 끝낼지 안끝낼지 또 보여줌
    fraction_bin = ''    # 2진수 01010101010 하나씩 더해줄거
    overflow = 13
    while count < overflow:       # overflow 안되었다면 while문 계속.
        addible = 1/(2**count)   # 2^count로 나누게 될테니 0.5 0.25 0.125 이렇게 나간다.
        if calculating + addible <= target: # 더할 수 있다면. (초과하지 않는다면)
            calculating += addible          # 누적합에 더해주고
            fraction_bin = fraction_bin + '1' # 더해줬으니 1 표시도 더해줌
        else:                              # 더할 수 없으니
            fraction_bin = fraction_bin + '0' # 0 더함
        if calculating == target:  # 누적합이 target과 같다면 (이쪽이 마지막 로직)
            return fraction_bin  # 끝내줄 분기 로직(이전 while 분기까지 더한 2진수표기 반환)
        count += 1                            # 다음자리수로 넘겨준다.
    return 'overflow'


T = int(input())

for case in range(1, T+1):
    N = float(input())
    print(f'#{case} {float_to_bin(N)}')