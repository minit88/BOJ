

n,k = map(int,input().split())
result = 0
coin_arr = []
for i in range(n):
    coin_arr.append(int(input()))

coin_arr.sort(reverse=True)

for i in range(n):
    if k >= coin_arr[i]:
        result += (k//coin_arr[i])
        k = (k%coin_arr[i])

print(result)
