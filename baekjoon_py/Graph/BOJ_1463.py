from collections import deque
n = int(input())
INF = float('inf')
num_list = [ INF for i in range(10**6+1)] # 각 숫자가 몇 번만에 왔는지 최소
q = deque([])
q.append((n,0))


while q:
    current_num, current_trying = q.popleft()

    if(1<=current_num<=10**6):
        if(num_list[current_num]>current_trying):
            num_list[current_num] = current_trying
            if (current_num%3 ==0):
                q.append((current_num//3,current_trying+1))
            if (current_num%2 ==0):
                q.append((current_num//2,current_trying+1))
            if (current_num>1):
                q.append((current_num-1,current_trying+1))
print(num_list[1])