import sys

input = sys.stdin.readline
n= int(input())

arr = list(int(input()) for _ in range(n))
arr.sort()

def solve(arr):

    i = 0
    result = float('inf')

    # 투 포인터
    for j in range(n):
        while arr[j]-arr[i]>4:
            i += 1

        current_length = j-i+1

        result = min(result, 5-current_length)
    return result

print(solve(arr))


