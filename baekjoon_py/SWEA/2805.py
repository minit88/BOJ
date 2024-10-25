
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
"""
         x,y 
n : 1 -> 0,0
n : 3 -> 1,1
n : 5 -> 2,2
n : 7 -> 3,3
n : 9 -> 4,4
"""

for test_case in range(1,T+1):
    """
    Input
    """
    n=int(input())
    array = []
    mid_idx = n//2
    result =0
    for i in range(n):
        int_list = []
        for input_str in list(str(input())):
            int_list.append(int(input_str))
        array.append(int_list)


    for i in range(n):
        d = abs(mid_idx - i)

        result+=sum(array[i][d:n-d])

    print("#%d %d" %(test_case,result))
