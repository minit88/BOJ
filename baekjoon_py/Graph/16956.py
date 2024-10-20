r,c = map(int,input().split())

array = []

for i in range(r):
    array.append(list(str(input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
wf = -1
for row in range(r):
    for col in range(c):
        if array[row][col] == 'S':
            for i in range(4):
                nx = dx[i] + row
                ny = dy[i] + col
                if 0<= nx < r and 0<= ny< c:
                    if array[nx][ny] =='W':
                        print(0)
                        wf= 0
                        break
                    elif array[nx][ny] == '.':
                        array[nx][ny] = 'D'
if wf== -1:
    print(1)
    for i in array:
        print("".join(map(str,i)))


