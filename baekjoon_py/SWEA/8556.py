T = int(input())

for test_case in range(1,T+1):
    """
    Input
    """
    input_dir = list(str(input()))
    dir_list = []

    for dir_str in input_dir:

        if (dir_str == 'n' or dir_str =='w'):
            dir_list.append(dir_str)

    """
    Solve
    """
    def divisor(n1,n2):
        while True:
            if n1%2 !=0 or n2%2 != 0 :
                return n1,n2
            else:
                n1 = n1//2
                n2 = n2//2

    a = 0
    if dir_list[-1] == 'w':
        a = 90

    dir_list.pop(-1)
    dir_list.reverse()

    n = 0
    result =""
    n1,n2 =0,0
    for dir_str in dir_list:
        n+=1
        if dir_str =='w':
            n1 = a*(2**n)+90
            n2 = 2**n
            a= (a+ (90/2**n))


        elif dir_str =='n':
            n1 = a*(2**n)-90
            n2 = 2**n
            a= (a-(90/2**n))
    a= int(a)

    if dir_list :
        n1,n2 = divisor(n1,n2)
        if int(n1)%int(n2) !=0:
            a= "%d/%d" %(n1,n2)

    print("#%d %s" %(test_case,a))

