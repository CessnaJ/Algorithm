# print(bin(0))
#
# def recursive(n):
# 	if n==1:
# 		return
# 	else:
# 		print(n)
# 		recursive(n-1)
# 		print(f'{n}th trial done')
#
#
# recursive(5)

dimension_matrix = [[0]*5 for _ in range(5)]

dimension_matrix[0][2:5] = [1]*3

print(dimension_matrix)