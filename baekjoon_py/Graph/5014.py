from collections import deque
f,s,g,u,d = map(int,input().split())

visited = [10**9 for i in range(f+1)]
#print(visited)
q= deque([])

q.append((s,0)) # 처음 위치, 버튼누른 횟수
visited[s] = 0

while q:
    nowNode, cnt = q.popleft()

    if nowNode == g:
        break

    # 각 노드를 방문할 때 버튼을 누른 횟수가 최소일 경우만 고려하면 됨 -> 최적의 경우
    for i in range(2):
        # U
        if i == 0 :
            nextNode = nowNode + u
        # D
        else:
            nextNode = nowNode - d

        # 범위 내이면 큐 삽입
        if 1<=nextNode<=f and nowNode != nextNode:
            if cnt+1<visited[nextNode]:
                # q삽입
                q.append((nextNode,cnt+1))
                # 방문 처리
                visited[nextNode] = cnt+1

if visited[g] == 10**9:
    result = "use the stairs"
else:
    result = visited[g]
print(result)

