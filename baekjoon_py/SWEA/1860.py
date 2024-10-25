#sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):

    """
    Input
    """
    n,m,k = map(int,input().split())

    sec_list = list(map(int,input().split())) # n개의 정수, 각 사람이 언제 도착하는지 초 단위


    """
    Solve
    """
    sec_list.append(0)
    sec_list.sort()

    cur_sec = 0
    cur_count = 0
    result = "Possible"


    for idx in range(1,n+1): # [ 1,15,20]
        cur_sec += sec_list[idx]-sec_list[idx-1] # 붕어빵 만들기 전까지 경과시간
        cur_count += ((cur_sec//m)*k)
        cur_sec -= cur_sec//m*m # 붕어빵 만들면 만든 수 만큼 누적시간 빼주기

        if (cur_count>=1):
            cur_count-=1
            continue
        else:
            result = "Impossible"
            break


    print("#%d %s" %(test_case, result))
