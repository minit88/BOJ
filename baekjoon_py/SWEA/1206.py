
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n= int(input()) # 건물 수

    h_list = list(map(int,input().split())) # 건물 높이 리스트
    result = 0
    if n==4:
        continue
    elif n==5:
        if h_list[2]>=1:
            result+=h_list[2]
    elif n>=6:
        for j in range(2,n-2): # 2부터 n-2 까지
            dl_dist1 = h_list[j]-h_list[j-1]
            dl_dist2 = h_list[j]-h_list[j-2]

            dr_dist1 = h_list[j]-h_list[j+1]
            dr_dist2 = h_list[j]-h_list[j+2]

            if dl_dist1 >0 and dl_dist2 >0 and dr_dist1 >0 and dr_dist2 >0:

                result += min(dl_dist1,dl_dist2,dr_dist2,dr_dist1)
            else:
                continue
    print("#%d %d"%(test_case,result))



