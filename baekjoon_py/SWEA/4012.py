from itertools import combinations
from copy import deepcopy
T = int(input())

def food_making(arr,case):
    res= 0
    for f1,f2 in combinations(case,2):
        res += arr[f1][f2] + arr[f2][f1]
    return res

for test_case in range(1,T+1):
    result = float('inf')
    n= int(input())
    array = []
    for i in range(n):
        array.append(list(map(int,input().split())))

    comb_idx_list = combinations([i for i in range(n)],n//2)
    for comb_idx1 in comb_idx_list:
        comb_idx2 = list(set(range(n)) - set(comb_idx1))

        food1_sg = food_making(array,list(comb_idx1))
        food2_sg = food_making(array,comb_idx2)

        result = min(result,abs(food1_sg-food2_sg))

    print("#%d %d" %(test_case,result))


