n = int(input())
result = float('inf')
arr = list(map(int, input().split()))
sorted_arr = []

for idx, val in enumerate(arr):
    is_plus = 1 # 1은 양수, -1은 음수
    if val < 0 :
        is_plus = -1
    sorted_arr.append((abs(val), is_plus))

sorted_arr.sort()

for i in range(len(sorted_arr)-1):
    a = sorted_arr[i]
    b = sorted_arr[i+1]
    sum_val = abs(a[0]*a[1]+b[0]*b[1])
    if sum_val < result:
        result = sum_val
        result_list = [a[0]*a[1], b[0]*b[1]]
        result_list.sort()

        result_a, result_b = result_list[0], result_list[1]


print(result_a, result_b)



