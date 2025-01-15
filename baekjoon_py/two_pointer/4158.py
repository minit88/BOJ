import sys

input = sys.stdin.readline

while True:
    n,m = map(int,input().split())

    if n == 0 and m== 0 :
        break

    cd_list_sang = []
    cd_list_sun = []


    for i in range(n):
        cd_list_sang.append(int(input()))

    for i in range(m):
        cd_list_sun.append(int(input()))


    now_sang_idx = 0
    now_sun_idx = 0
    result = 0


    while now_sang_idx < n and now_sun_idx < m:
        cd_sang = cd_list_sang[now_sang_idx]
        cd_sun = cd_list_sun[now_sun_idx]
        if cd_sang == cd_sun:
            result += 1
            now_sang_idx += 1
            now_sun_idx += 1

        elif cd_sang > cd_sun:
            now_sun_idx += 1
        elif cd_sang < cd_sun:
            now_sang_idx += 1


    print(result)


