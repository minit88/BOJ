T= int(input())

for test_case in range(1,T+1):
    n= int(input())

    s1 = n*(n+1)//2
    s2 = (n*(2+(n-1)*2))//2
    s3 = n*(n+1)

    print("#%d %d %d %d" %(test_case,int(s1),int(s2),int(s3)))


