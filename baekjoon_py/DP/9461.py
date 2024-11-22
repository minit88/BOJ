T = int(input())
for test_case in range(1,T+1):
    n = int(input())

    array = [0,1,1,1]

    if n in [1,2,3]:
        print(1)
    else:
        for idx in range(4,n+1):
            array.append(array[idx-3]+array[idx-2])
        print(array[-1])