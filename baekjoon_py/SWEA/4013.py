from collections import deque
T = int(input())

for test_case in range(1,T+1):
    k = int(input())

    mag_array=[deque([])]


    for i in range(4):
        mag_array.append(deque(list(map(int,input().split()))))

    for i in range(k):
        lot_array = deque([])
        m,d = map(int,input().split())
        lot_array.append((m,d))

        now_m = m
        now_d = d
        # 왼쪽으로 회전 검사
        while True:
            next_m = now_m -1
            if now_d == 1:
                next_d = -1
            else:
                next_d = 1

            if now_m == 1:
                break
            else:
                if mag_array[now_m][6] != mag_array[next_m][2]:
                    lot_array.append((next_m,next_d))
                    now_d = next_d
                    now_m = next_m
                else:
                    break

        # 오른쪽 회전 검사
        now_m = m
        now_d = d
        while True:
            next_m = now_m +1
            if now_d == 1:
                next_d = -1
            else:
                next_d = 1

            if now_m == 4:
                break
            else:
                if mag_array[now_m][2] != mag_array[next_m][6]:
                    lot_array.append((next_m,next_d))
                    now_d = next_d
                    now_m = next_m

                else:
                    break

        while lot_array:
            m,d = lot_array.popleft()
            if d == 1:
                mag_array[m].appendleft(mag_array[m].pop())
            else:
                mag_array[m].append(mag_array[m].popleft())



    result = 0
    for i in range(4):
        if mag_array[i+1][0] == 1:
            result += 2**(i)

    print("#%d %d" %(test_case,result))


