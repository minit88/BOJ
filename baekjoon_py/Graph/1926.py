from collections import deque

n,m = map(int,input().split())
array = []

pict_cnt = 0 # 그림 개수
ext = 0 # 넓이

visited = [[-1 for i in range(m)] for _ in range(n)]

for i in range(n):
    array.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(m):
        if visited[i][j] != 0 and array[i][j] == 1:
            pict_cnt += 1
            now_ext = 1

            q= deque([])
            q.append((i,j))
            visited[i][j] = 0

            while q:
                x,y = q.popleft()

                for d in range(4):
                    nx = x+dx[d]
                    ny = y+dy[d]
                    if 0<= nx <n and 0<= ny <m and array[nx][ny] == 1 and visited[nx][ny] != 0:
                        now_ext+=1
                        visited[nx][ny] = 0
                        q.append((nx,ny))
            ext = max(ext,now_ext)
        else:
            continue

print(pict_cnt)
print(ext)
