for i in range(1,11):
    result = -1*float('inf')
    test_case_num = int(input())

    num_array = []
    # input을 받기
    for k in range(100):
        num_list = list(map(int,input().split()))
        num_array.append(num_list)

    # 가로 행 계산
    for x in range(100):
        sum_row = 0
        for y in range(100):
            sum_row += num_array[x][y]
        result = max(sum_row, result)

    # 세로 열 계산
    for y in range(0,100):
        sum_col=0
        for x in range(0,100):
            sum_col += num_array[x][y]

        result = max(sum_col, result)

    # 대각선 계산
    sum_lr = 0
    sum_rl = 0
    for idx in range(0,100):
        sum_lr += num_array[idx][idx]
        sum_rl += num_array[idx][99-idx]

    result = max(sum_lr,result)
    result = max(sum_rl,result)


    # 결과 출력
    print("#%d %d" %(test_case_num,result))





