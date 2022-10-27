# dp적으로 풀어보자. 1x1 확인해서 정사각형 만족하면 1 저장. 2x2확인해서 만족하면 4 저장 이런식으로 쭉쭉..

# 저장 할 매트릭스 따로 또 만들어 줘야함.
from sys import stdin

rows, cols = map(int, input().split())

matrix = [map(int, stdin.readline().split()) for _ in range(rows)]

