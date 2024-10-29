T = int(input())
result = []

for test_case in range(1, T + 1):
    n = int(input())

    if n == 0:
        sum_num = 0
    else:
        sum_num = n % 9 if n % 9 != 0 else 9

    result.append("#%d %d" % (test_case, sum_num))

# 한 번에 결과 출력
print("\n".join(result))