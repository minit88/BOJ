from collections import deque
n=int(input())

array = [[0 for i in range(n)] for j in range(n)]

find_num= int(input())
num = n**2
dx = [1,0,-1,0]
dy = [0,1,0,-1]


q= deque([])
q.append((0,0))

result_x,result_y =1,1

while q:
    x,y = q.popleft()
    start_x,start_y = x,y

    if 0<=x<n and 0<=y<n:
        if array[x][y]==0:
            if find_num == num:
                result_x+=x
                result_y+=y
            array[x][y]+=num
            num-=1

        for i in range(4):
            while True:
                x, y = dx[i]+x, dy[i]+y

                if 0<=x<n and 0<=y<n :
                    if array[x][y] ==0:
                        if find_num == num:
                            result_x+=x
                            result_y+=y
                        array[x][y] += num

                        num-=1
                    else:
                        x-=dx[i]
                        y-=dy[i]
                        break
                else:
                    x-=dx[i]
                    y-=dy[i]
                    break
    if 0<=start_x+1<n and 0<=start_y+1<n:
        if array[start_x+1][start_y+1] == 0:
            q.append((start_x+1,start_y+1))


for i in range(n):
    print(" ".join(map(str,array[i])))
print(result_x,result_y)