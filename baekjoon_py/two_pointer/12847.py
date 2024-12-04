import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num_arr = list(map(int,input().split()))
current_sum = sum(num_arr[:m])
if m==n :
    print(current_sum)
else:
    max_sum = current_sum

    for i in range(m,n):
        current_sum += num_arr[i] - num_arr[i-m]
        max_sum = max(max_sum,current_sum)

    print(max_sum)


