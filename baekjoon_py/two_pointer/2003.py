import sys

input = sys.stdin.readline
n, m = map(int, input().split())
num_arr = list(map(int, input().split()))

start, end = 0,0
current_sum = 0 # 부분합
cnt = 0

while end <= n:
    if current_sum == m:
        # 부분합이 m과 동일하면 cnt+=1, start 오른쪽으로 이동
        cnt += 1
        current_sum -= num_arr[start]
        start +=1
    elif current_sum > m:
        # 부분합이 m보다 크면 start 오른쪽으로 이동
        current_sum -= num_arr[start]
        start +=1
    elif current_sum < m:
        # 부분합이 m보다 작으면 end 오른쪽으로 이동
        if end<n:
            current_sum += num_arr[end]
        end += 1
print(cnt)


