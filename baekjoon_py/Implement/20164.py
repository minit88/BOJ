
def find_max_min(num,cnt):

    global min_cnt
    global max_cnt

    for digit in str(num):
        if int(digit) % 2 == 1:
            cnt += 1

    if num< 10:
        min_cnt = min(min_cnt,cnt)
        max_cnt = max(max_cnt,cnt)
        return

    elif num<100:
        num1 = int(str(num)[0])
        num2 = int(str(num)[1])
        find_max_min(num1+num2,cnt)
    else:
        num_str = str(num)
        length = len(num_str)

        for i in range(1,length-1):
            for j in range(i+1,length):
                num1 = int(num_str[:i])
                num2 = int(num_str[i:j])
                num3 = int(num_str[j:])
                find_max_min(num1+num2+num3,cnt)


n= int(input())

min_cnt = float('inf')
max_cnt = float('-inf')

find_max_min(n,0)

print(min_cnt,max_cnt)