from collections import deque
import heapq
n,k = map(int,input().split())

jewel_arr = [] # 무게, 가격
bag_arr = [] # 무게
result = 0 # 출력 값

for i in range(n):
    m,v = map(int,input().split())
    jewel_arr.append((m,v))

for i in range(k):
    bag_arr.append(int(input()))

bag_arr.sort()
jewel_arr.sort()
max_heap = []

jewel_q= deque(jewel_arr)

for limit_weight_bag in bag_arr:
    while jewel_q:
        weight, price = jewel_q.popleft()
        if limit_weight_bag>=weight:
            heapq.heappush(max_heap,-price)
        else:
            jewel_q.appendleft((weight,price))
            break
    if max_heap:
        result += -heapq.heappop(max_heap)
print(result)

