import sys

input = sys.stdin.readline

n,k = map(int,input().split())
num_arr = list(map(int,input().split()))

result= float('-inf')

current_sum = sum(num_arr[:k])
result =max(result,current_sum)
start = 0
if k==n:
    result = sum(num_arr)
else:
    for i in range(k,n):

        current_sum -= num_arr[start]
        current_sum += num_arr[i]
        result = max(result, current_sum)

        start +=1

print(result)