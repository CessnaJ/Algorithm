how_many_color_paper = int(input())
paper_num_coordinates = dict.fromkeys(range(1, how_many_color_paper + 1), [])
max_coor = 0
for i in range(1, how_many_color_paper+1):
    coor_at_point = list(map(int, input().split()))
    coor_modified = [coor_at_point[0], coor_at_point[1], coor_at_point[0]+coor_at_point[2], coor_at_point[1]+coor_at_point[3]]
    if max(coor_modified) > max_coor:
        max_coor = max(coor_modified)
    paper_num_coordinates[i] = coor_at_point

background = [[0]*(max_coor) for _ in range(max_coor)]

for key in range(1, how_many_color_paper + 1):
    for row in range(paper_num_coordinates[key][0], paper_num_coordinates[key][0]+paper_num_coordinates[key][2]):
        for col in range(paper_num_coordinates[key][1], paper_num_coordinates[key][1]+paper_num_coordinates[key][3]):
            background[row][col] = key


area_by_key = dict.fromkeys(range(0, how_many_color_paper + 1), 0) #0은 안그려진 거니까 그거 보여주려고 0도 추가

for row in range(max_coor):
    for col in range(max_coor):
        area_by_key[background[row][col]] += 1

for value in range(1, how_many_color_paper + 1):
    print(area_by_key[value])