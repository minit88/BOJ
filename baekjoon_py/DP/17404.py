n = int(input())
rgb_arr =[]

INF = 10**9
result = INF
for i in range(n):
    rgb_arr.append(list(map(int,input().split())))

for k in range(3):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][k] = rgb_arr[0][k]

    for i in range(1,n):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2])+rgb_arr[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2])+rgb_arr[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1])+rgb_arr[i][2]
    for i in range(3):
        if i!=k:
            result = min(result, dp[n-1][i])
print(result)

