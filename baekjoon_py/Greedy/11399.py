
n= int(input())
delay_time_arr = list(map(int, input().split()))
result = 0
delay_time_arr.sort()
for i in range(n):
    result += sum(delay_time_arr[:i+1])

print(result)