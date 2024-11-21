"""
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
"""
"""
백트래킹으로 현재 숫자가 n 보다 작은 경우 계속 반복 -> n 이면 result +=1
"""

num_arr = [1,2,3]

def back_tracking(now_num):
    global result

    if now_num == n:
        result +=1
        return 0

    for i in range(len(num_arr)):
        next_num = now_num+num_arr[i]
        if next_num <= n:
            back_tracking(next_num)


T = int(input())

for test_case in range(1,T+1):
    result = 0
    n = int(input())

    back_tracking(0)

    print(result)

