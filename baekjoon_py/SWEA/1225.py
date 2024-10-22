"""
주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.
- 8개의 숫자를 입력받는다
- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
  다음 첫 번째 숫자는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소 .. 그다음 4 그다음 6 이와 같은 작업을 한 사이클이라 한다.
"""

for _ in range(10):
    test_case = int(input())
    num_list = list(map(int,input().split()))

    cycle = 0

    while True:
        current_num =0
        if cycle == 5 :
            cycle = 0

        current_num = num_list.pop(0)
        # -1
        if cycle == 0:
            current_num-=1
        # -2
        elif cycle == 1:
            current_num-=2
        # -3
        elif cycle ==2:
            current_num-=3

        elif cycle == 3:
            current_num-=4

        elif cycle == 4:
            current_num-=5

        if current_num <= 0:
            num_list.append(0)
            break
        else:
            num_list.append(current_num)
            cycle+=1
    result = "#%d" %(test_case)
    for num in num_list:
        result += " %d" %(num)

    print(result)



