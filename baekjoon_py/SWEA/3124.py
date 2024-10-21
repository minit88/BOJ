T=int(input())
for testCase in range(1,T+1):
    V,E = map(int,input().split())
    parent = [0]*(V+1)
    result = 0
    for i in range(1,V+1):
        parent[i]=i # 초기 부모는 자기 자신

    def find_parent(x):
        if parent[x]!=x : # 자기 자신일 경우 리턴
            parent[x]= find_parent(parent[x]) # 최종 출력값은 재귀호출
        return parent[x]

    def union_parent(x,y):
        x_parent= find_parent(x)
        y_parent= find_parent(y)

        if y_parent>x_parent : # y의 부모가 x 보다 크면 y 부모는 x의 부모
            parent[y_parent]=x_parent
        else: # x의 부모가 y보다 크면 x의 부모는 y 부모
            parent[x_parent]=y_parent

    node_list = []
    for i in range(E):
        A,B,C = map(int,input().split())
        node_list.append([A,B,C])
    node_list.sort(key=lambda n: (n[2]))

    for node in node_list:
        n1,n2,cost = node
        if find_parent(n1)!=find_parent(n2):
            result += cost
            union_parent(n1,n2)
    print("#%d %d" %(testCase,result))

