
n,s = map(int,input().split())

input_arr = list(map(int,input().split()))
min_length = float('inf')
cur_sum, start = 0,0

for end in range(len(input_arr)):
    cur_sum += input_arr[end]

    while cur_sum >= s:
        min_length = min(min_length, end-start+1)
        cur_sum -= input_arr[start]
        start +=1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)

