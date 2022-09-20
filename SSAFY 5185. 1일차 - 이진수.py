T = int(input())

for case in range(1, T+1):
    n_hexadecimal =input().split() # 여기서 30분을 사용했다. 다음번에도 이런일이 있을것이다. 그냥 (2번째 글자부터 받으면 n이 10이 되었을때 한글자씩 밀려서 slicing에서 문제가 생긴다.)
    hex_to_int = int(n_hexadecimal[1], 16) # 16진법으로 인식시키는 explicit expression

    binary = bin(hex_to_int)                # 2진법으로 전환

    bin_sig_figure = str(binary)[2:]         # 0b는 안쓸거

    answer = ((-len(bin_sig_figure) % 4) * '0') + bin_sig_figure # modulo를 이용하면 4글자씩 끊어지는거에서 몇글자가 빠졌는지 채우는게 가능하다,
    # 음수를 이용해서 modulo를 쓰면 floor 연산을 하기 때문에 몇글자가 빠졌는지 계산할 수 있다.

    print(f'#{case} {answer}')
