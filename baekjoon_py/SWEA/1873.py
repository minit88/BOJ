
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    """
    input
    """
    H,W = map(int,input().split()) # 세로, 가로

    map_array = []
    for i in range(H):
        map_array.append(list(str(input())))


    N = int(input())
    comm_list = list(str(input()))

    y = -1
    x = -1
    dir = -1 # 0, 1, 2, 3 -> 동, 서, 북, 남
    dir_list = [(0,1),(0,-1),(-1,0),(1,0)] # y,x
    dir_str_list = ['>','<','^','v']

    for i in range(H):
        for j in range(W):
            if map_array[i][j] == '<' :
                y = i
                x = j
                dir = 1
            elif map_array[i][j] == '>' :
                y = i
                x = j
                dir = 0
            elif map_array[i][j] == 'v' :
                y = i
                x = j
                dir = 3
            elif map_array[i][j] == '^':
                y = i
                x = j
                dir = 2

    while comm_list:
        cur_comm = comm_list.pop(0)
        # 포탄 발사
        if cur_comm == 'S':
            dy, dx = dir_list[dir]
            shot_x =0
            shot_y =0

            shot_x +=x
            shot_y +=y

            while True:
                if 0<=shot_x+dx<W and 0<=shot_y+dy<H:
                    if map_array[shot_y+dy][shot_x+dx] == '.' or map_array[shot_y+dy][shot_x+dx] == '-':
                        shot_x += dx
                        shot_y += dy
                    elif map_array[shot_y+dy][shot_x+dx] == '*':
                        map_array[shot_y+dy][shot_x+dx] = '.'
                        break
                    else:
                        break
                else:
                    break
       # 이동
        else:
            if cur_comm == 'U':
                dir  = 2
            elif cur_comm == 'D':
                dir = 3
            elif cur_comm == 'L':
                dir = 1
            elif cur_comm == 'R':
                dir = 0
            map_array[y][x] = dir_str_list[dir]

            # 전차 이동
            dy, dx = dir_list[dir]

            if 0<=y+dy<H and 0<=x+dx<W:
                if map_array[y+dy][x+dx] == '.':
                    map_array[y][x] = '.'
                    map_array[dy+y][dx+x] = dir_str_list[dir]
                    x = x+dx
                    y = y+dy

    result_map= ""
    for i in map_array.pop(0):
        result_map+= i
    print("#%d %s" %(test_case, result_map))
    if map_array:
        for i in map_array:
            result_map=""
            for j in i:
                result_map+=j
            print(result_map)



