#import sys
#input = sys.stdin.readlines

n= int(input())
num_arr = list(map(int, input().split()))
x = int(input())
start = 0
end = n-1
result = 0
num_arr.sort()

while True:
    if (0<= start<n and 0<= end<n) and start<end:
        current_sum = num_arr[start] + num_arr[end]
        if current_sum == x:
            result +=1
            end -=1
        elif current_sum > x:
            end -=1
        elif current_sum < x:
            start +=1
    else:
        break



print(result)