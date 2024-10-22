import heapq

n= int(input())

heap = []

result = []

number_idx = 0
for i in range(n):
    x = int(input())

    if x!= 0:
        heapq.heappush(heap,(abs(x),x))

    elif x==0:
        if heap:
            out_num = heapq.heappop(heap)
            result.append(out_num[1]) # 이전 x 대입
        else:
            result.append(0)

for i in result:
    print(i)


