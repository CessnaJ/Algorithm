# import math
# # print(bin(0))
# #
# # def recursive(n):
# # 	if n==1:
# # 		return
# # 	else:
# # 		print(n)
# # 		recursive(n-1)
# # 		print(f'{n}th trial done')
# #
# #
# # recursive(5)
# #
# # dimension_matrix = [[0]*5 for _ in range(5)]
# #
# # dimension_matrix[0][2:5] = [1]*3
# #
# # # print(dimension_matrix)
# #
# # lst1 = []
# #
# #
# # def test(a):
# #     return None
# #
# # lst1.append(test('b'))
# # lst1.append(test('b'))
# # lst1.append(test('b'))
# #
# # print(lst1)
# #
# a = -1
# b = 1
#
# print(math.degrees(math.atan(b/a)))
# print(math.degrees(math.atan(-1)))
# print(math.degrees(math.atan2(1,-1)))
#
# # 내 목적구에 대해서만
#     for obj in objball:
#     	#후보가 될 path들
#         cand_path = []
#         # 모든 홀에 대해서 (6개)
#         for hole in Myholes:
#             #obj이 hole에 가는 방법
#             objtohole = path_find(obj,hole)
#             # path_find 함수는 obj-hole 백터를 반환하며 공의 진행방향에 장애물이 있나 확인
#             if not objtohole:
#                 print('not objtohole pass')
#                 continue
#             # objtohole을 위해 수구의 도착 위치 계산
#             objtohole_nv = objtohole/(objtohole.norm)
#             # 목적구가 홀로 가려는 방향의 반대방향으로
#             #공크기만큼 이동한 점이 수구가 가야할 곳
#             que = obj + Ball_R*-objtohole_nv
#             # 수구 to que점을 가는 길 계산
#             quetoobj = path_find(myball,que)
#             if not quetoobj:
#                 print('no quetoobj pass')
#                 continue
#             quetoobj_nv = quetoobj/(quetoobj.norm)
#             # 두 백터의 각도 계산 (단위백터끼리의 내적 cos(theta) 값임)
#             # 영보다 작거나 음수면 안하고 진행
#             if objtohole_nv.dot(quetoobj_nv) <= 0:
#                 continue
#             #weights *= objtohole_nv.dot(quetoobj_nv)
#
#             # 예측 힘의 값, objtohole 거리, quetoobj 거리에 비례하게 함
#
#             mue = 5.5
#             v1h = (55+2*mue*objtohole.norm)
#             v01 = (v1h+2*mue*quetoobj.norm)**(1/2)
#             inferF = quetoobj_nv * v01
#             # 앞선 각도를 계산한 내적 값을 나눠주어 각도가 얇다면 더 쎄게 치도록 함
#             inferF = inferF/(objtohole_nv.dot(quetoobj_nv)**(1/2))
#             # 완성된 패스를 등록
#             # 등록할 때 각도가 두꺼운 것을 우선하도록
#             # 하지만 적당히 두꺼운 각도면 수용하도록 각도를 integer화함
#             cand_path.append([int(objtohole_nv.dot(quetoobj_nv)*10),inferF.norm,inferF])
# 		# 모든 Hole에 대한 연산이 끝나면
#         # cand_path를 정렬하여 가장 각도가 두껍고 힘이 약한 것을
#         cand_path.sort(key=lambda x : (-x[0],x[1]))
#         if cand_path:
#         #Pathlist에 넣는다. cand_path는 한 목적구에 대한 계산임
#             Pathlist.append(cand_path[0])
#
# 	#Pathlist는 모든 목적구에 대한
#     #가장 일직선으로 만나는 것 + 다음으로 힘의 필요가 가장 작은 것을 쓰자
#     Pathlist.sort(key=lambda x : (-x[0],x[1]))



