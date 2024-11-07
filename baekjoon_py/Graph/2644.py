from collections import deque

num_per = int(input())
p1,p2 = map(int, input().split())

array = [[] for _ in range(num_per+1)]
parent = [i for i in range(num_per+1)]


n = int(input())
result =-1

def bfs(start,end):
    global result
    visited = [0 for _ in range(num_per+1)]

    q= deque([])
    if parent[start] == start :
        q.append((start,0))
    else:
        q.append((parent[start],1))
        visited[parent[start]]=1

    visited[start] = 1

    while q:
        node, cost = q.popleft()

        if node == end:
            result = cost
            return 0
        else:
            # 부모와 자식들 다시 q에 넣어야 함
            node_parent = parent[node]
            if visited[node_parent] == 0:
                q.append((node_parent,cost+1))
                visited[node_parent] = 1

            for child_node in array[node]:
                if visited[child_node] == 0:
                    q.append((child_node,cost+1))
                    visited[child_node] = 1

for i in range(n):
    x,y = map(int,input().split())
    array[x].append(y)
    parent[y] = x

bfs(p1,p2)
print(result)