from collections import deque
n=int(input())

array = [[] for _ in range(n+1)]
result = 0

for i in range(int(input())):
    a,b = map(int,input().split())
    array[a].append(b)
    array[b].append(a)

visited = [i for i in range(n+1)]


q = deque([])
q.append((1,0))
visited[1]=0

while q:
    node,cost = q.popleft()
    #print(node,cost)

    if cost<2:
        for next_node in array[node]:
            if visited[next_node] != 0:
                result+=1
                q.append((next_node,cost+1))
                visited[next_node] = 0 # 방문 처리

            elif visited[next_node] == 0:
                continue

print(result)