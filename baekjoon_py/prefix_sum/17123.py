T= int(input())

for test_case in range(1,T+1):
    n,m=map(int,input().split())

    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))

    prefix_sum = []

    for i in range(2):
        # 가로 합
        if i == 0:
            prefix_array= []
            for idx in range(n):
                prefix_array.append(sum(array[idx][:]))

        # 세로 합
        elif i ==1:
            prefix_array= []
            for col in range(n):
                sum_num = 0
                for row in range(n):
                    sum_num+=array[row][col]

                prefix_array.append(sum_num)

        prefix_sum.append(prefix_array)


    for _ in range(m):
        r1, c1, r2, c2, v  = map(int,input().split())
        sum_r = (c2-c1+1)*v
        sum_c = (r2-r1+1)*v
        # 가로 합
        for n in range(r2-r1+1):
            prefix_sum[0][r1+n-1] += sum_r
        # 세로 합
        for n in range(c2-c1+1):
            prefix_sum[1][c1+n-1] += sum_c

    for i in range(2):
        print(" ".join(map(str,prefix_sum[i][:])))