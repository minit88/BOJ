
def set_password(array):
    flg = -1
    next_array = []
    for i in range(len(array)-1):
        if 0<i+1<len(array):
            if array[i]==array[i+1]:
                flg = 0
                next_array += array[:i]
                if 0<i+2<len(array):
                    next_array += array[i+2:]
                break

    if flg == -1:
        return array
    elif flg == 0:
        return set_password(next_array)



for test_case in range(1,10+1):
    array_len, array = map(str,input().split())
    array_len = int(array_len)
    array = list(map(int,array))

    print("#%d %s" %(test_case, "".join(map(str,set_password(array)))))


