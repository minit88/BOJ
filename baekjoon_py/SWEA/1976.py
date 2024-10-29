T = int(input())

for test_case in range(1,T+1):
    h1,m1,h2,m2 = map(int,input().split())

    min = m1 + m2
    hour = h1 + h2

    if (min>=60):
        hour += min//60
        min = (min%60)

    if hour==24:
        hour = 12
    elif hour>12:
        hour = hour%12

    print("#%d %d %d" %(test_case,hour,min))