import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    array = list(map(int, input().split()))
    array.reverse()

    max_price = array[0]

    current_total_buy = 0 # 구매 가격
    current_total_count = 0 # 구매 수량

    result = 0

    start = 0

    for i in range(1,n):

        # 정산
        if array[i] > max_price:

            if current_total_count>=1:
                result += (current_total_count*max_price - current_total_buy)

                current_total_count,current_total_buy = 0,0

            max_price = array[i]

        # 구매
        elif array[i]<=max_price:
            current_total_count += 1
            #print(array[i])
            current_total_buy += array[i]

    if current_total_count >=1:
        result += (current_total_count*max_price - current_total_buy)





    print("#%d %d" % (test_case, result))
