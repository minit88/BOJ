import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())

result = []
inDegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
q = deque([])
for i in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)
    inDegree[b] += 1

def topology_sort(q):
    while q:
        now = q.popleft()
        result.append(now)

        for n in graph[now]:
            inDegree[n] -=1
            if inDegree[n] == 0:
                q.append(n)

for i in range(1,n+1):
    if inDegree[i] == 0:
        q.append(i)

topology_sort(q)
print(" ".join(map(str,result)))