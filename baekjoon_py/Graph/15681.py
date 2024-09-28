from sys import stdin,setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline  # sys.stdin.readline 사용

n, r, q = map(int, input().split())
edges = [[] for _ in range(n + 1)]  # 간선정보 저장
for _ in range(n - 1):
    u, v = map(int, input().split())
    # 양방향
    edges[u].append(v)
    edges[v].append(u)

size = [0] *(n+1)

visited = [False] *(n+1)

def dfs(node):
    visited[node] = True
    size[node] = 1
    for edge in edges[node]:
        if not visited[edge]:
            size[node] += dfs(edge)
    return size[node]

dfs(r)

for _ in range(q):
    query = int(input())
    print(size[query])
