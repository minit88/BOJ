from copy import deepcopy
from itertools import combinations

T = int(input())
def work(array):
    x,y = -1,-1
    result = float('-inf')

    for i in range(n):
        for j in range(n):
            # 현재 idx에서 m개 만큼 확인
            if j+m-1 <n and -1 not in array[i][j:j+m]:
                for cnt in range(1,m+1):
                    for comb in combinations(array[i][j:j+m],cnt):
                        now_result = 0
                        if sum(comb) <= c:
                            for val in comb:
                                now_result += val**2
                            if now_result>result:
                                result = now_result
                                x,y = i,j
                        else:
                            continue

    for i in range(y,y+m):
        array[x][i] = -1

    return result

for test_case in range(1,T+1):
    n,m,c = map(int,input().split())

    array = []
    result2 = 0
    for i in range(n):
        array.append(list(map(int,input().split())))

    for i in range(2):
        result2 += work(array)

    print("#%d %d" %(test_case,result2))

