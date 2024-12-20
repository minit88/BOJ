import sys

input = sys.stdin.readline

n= int(input())
m = int(input())
num_arr = list(map(int, input().split()))

# 숫자 오름차 순 정렬
num_arr.sort()

start = 0
end = n-1
result = 0

# end가 start보다 클 경우만 반복
while start<end:
    # 두 재료 합 계산
    current_sum = num_arr[start] + num_arr[end]

    # 두 재료 합이 m과 같을 경우 결과 +1, end -=1
    if current_sum == m:
        result += 1
        end -= 1

    # 재료 합이 m보다 클 경우 end -=1
    elif current_sum > m:
        end -= 1

    # 재료 합이 m보다 작을 경우 start -=1
    elif current_sum < m:
        start += 1
print(result)