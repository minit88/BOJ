
def find_parent(now_node):
    if parent[now_node] == now_node:
        return now_node
    else:
        return find_parent(parent[now_node])

def union_parent(x,y):
    parent_x = find_parent(x)
    parent_y = find_parent(y)

    if parent_x<parent_y:
        parent[parent_y]=parent_x
    else:
        parent[parent_x]=parent_y

n,m = map(int,input().split())

parent = [i for i in range(n+1)]
edges = []

for i in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()
result = 0
max_cost = 0
for edge in edges:
    cost,a,b = edge

    if find_parent(a)!=find_parent(b):
        result += cost
        union_parent(a,b)
        max_cost = cost

# 두 개의 마을로 분리하길 원했으니 마지막 간선의 비용을 빼주면 됨.
print(result-max_cost)
