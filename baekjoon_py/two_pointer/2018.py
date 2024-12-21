import sys

input = sys.stdin.readline

n = int(input())
num_arr = [i for i in range(0,n)]

start = 1
end = 1
current_sum = 0
result = 1

while end<=n:
    if current_sum == n:
        current_sum -= num_arr[start]
        start += 1
        result += 1
        #print("start: %d, end : %d" %(start, end))

    elif current_sum < n:
        if end<n:
            current_sum += num_arr[end]
        end += 1

    elif current_sum > n:
        if start < end:
            current_sum -= num_arr[start]
            start += 1
        else:
            break
print(result)


