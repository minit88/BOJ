
n,m = map(int,input().split())
num_list = list(map(int,input().split()))
num_sum_list = [0 for i in range(n)]
num_sum_list[0]+=num_list[0]
for i in range(1,n):
    num_sum_list[i]+= (num_sum_list[i-1]+num_list[i])
for idx in range(m):
    i,j = map(int,input().split())

    print(num_sum_list[j-1]-num_sum_list[i-1]+num_list[i-1])

"""
5 3
5 4 3 2 1
1 3
2 4
5 5
"""
