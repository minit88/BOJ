array = [[]]
for i in range(19):
    array.append([0]+list(map(int,input().split())))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
result = 0
result_x,result_y = 0,0
flg = -1
for x in range(1,20):
    if flg == 0 :
        break
    for y in range(1,20):
        if flg == 0:
            break
        color = array[x][y]
        # 빈 공간이면 건너뜀
        if color == 0:
            continue

        # 방향 8가지 조회
        for d in range(8):
            if flg == 0:
                break
            cnt = 1
            now_x, now_y = 0, 0
            now_x += x
            now_y += y

            while True:
                now_x += dx[d]
                now_y += dy[d]
                if 1<=now_x<20 and 1<=now_y<20 and array[now_x][now_y]==color:
                    cnt +=1
                else:
                    if cnt == 5:
                        if d>=4 :
                            if (1<=x+dx[d-4]<20 and 1<=y+dy[d-4]<20 and array[x+dx[d-4]][y+dy[d-4]] != color) or not (1<=x+dx[d-4]<20 and 1<=y+dy[d-4]<20):
                                result = color
                                if y<=now_y-dy[d]:
                                    result_x+= x
                                    result_y += y
                                else:
                                    result_x += now_x-dx[d]
                                    result_y += now_y-dy[d]
                                flg = 0
                    break
print(result)
if result in [1,2]:
    print(result_x,result_y)