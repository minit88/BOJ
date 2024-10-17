from collections import deque

n,k = map(int,input().split()) # 수 n 동 k
q = deque([])
INF = float('inf')
result = INF

q.appendleft([n,0,0]) # 현재 위치, 시간
time_list = [10**8 for _ in range(100001)]
# 0 : 시작, 1 : n+1, 2 : n-1, 3 : n*2
while q:
    c,t,f = q.popleft() # 현재 위치, 시간, 케이스
    if c == k : # 위치 도착하면 종료
        continue

    if 0<=c<=100000:
        if f != 2: # n-1 제외
            if (0<=c+1<=100000) and time_list[c+1]>t+1:
                q.append((c+1,t+1,1))
                time_list[c+1]= t+1

        if f != 1: # n+1 제외
            if (0<=c-1<=100000) and time_list[c-1]>t+1:
                q.append((c-1,t+1,2))
                time_list[c-1]= t+1
        if (0<=c*2<=100000):
            if time_list[c*2]>t+1:
                q.append((c*2,t+1,3))
                time_list[c*2]= t+1

    else:
        continue



print(time_list[k])