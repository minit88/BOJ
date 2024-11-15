from collections import deque
n,m = map(int,input().split())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

visited = [[0 for i in range(m)] for _ in range(n)] # 방문 정보 및 섬 정보

islCrd = [[]] # n 번째 섬 좌표들

islNum = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs -> 섬 정보 찾기
for x in range(n):
    for y in range(m):
        crdList = []
        if arr[x][y] == 1 and visited[x][y] == 0:
            crdList.append((x,y))

            q = deque([])
            q.append((x,y))

            visited[x][y] = islNum

            while q:
                now_x, now_y = q.popleft()

                for i in range(4):
                    next_x = now_x + dx[i]
                    next_y = now_y + dy[i]

                    if 0<= next_x<n and 0<= next_y<m and visited[next_x][next_y] == 0 and arr[next_x][next_y] == 1:
                        crdList.append((next_x,next_y))
                        q.append((next_x,next_y))
                        visited[next_x][next_y] = islNum

            islCrd.append(crdList)
            islNum += 1
        else:
            continue


# MST
def find_parent(a):
    if parent[a] == a:
        return a
    else:
        return find_parent(parent[a])

def union_parent(a,b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    elif parent_b < parent_a:
        parent[parent_a] = parent_b

islNum -=1
minBrgCnt = 0
edges =[] # 간선 리스트 cost, a, b
parent = [i for i in range(islNum+1)]

# 다리 놓고 간선 정보 가져오기
# 현재 섬이 1이면 다리 0
if islNum == 1:
    pass
else:
    for i in range(1,islNum+1):
        for j in islCrd[i]:
            for d in range(4):
                now_x, now_y = j
                next_x, next_y = 0,0
                next_x += now_x
                next_y += now_y
                nowBrdCnt = 0
                while True:
                    next_x += dx[d]
                    next_y += dy[d]

                    if 0<=next_x<n and 0<=next_y<m :
                        if visited[next_x][next_y] not in [0,i] :
                            if nowBrdCnt > 1:
                                edges.append((nowBrdCnt,i,visited[next_x][next_y])) # cnt, a, b
                            break
                        elif visited[next_x][next_y] == 0:
                            nowBrdCnt +=1
                        else:
                            break
                    else:
                        break

#edges = list(edges)
edges.sort()

mst_edges= 0
if edges:
    for edge in edges:
        cost,a,b = edge

        if find_parent(a) != find_parent(b):
            union_parent(a,b)
            minBrgCnt += cost
            mst_edges += 1

if mst_edges != islNum-1 or minBrgCnt == 0:
    minBrgCnt = -1


print(minBrgCnt)
