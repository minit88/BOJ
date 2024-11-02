# combinations 을 사용한 풀이
"""

from itertools import combinations
while True:
    n1_array= list(map(int,input().split()))

    n1_len = n1_array.pop(0)

    if n1_len == 0:
        break

    for i in combinations(n1_array,6):
        print(" ".join(map(str,i)))
    print("")
"""

# 재귀 호출하여 푼 풀이 // 재귀 호출 -> (현재 리스트,idx+1), (추가한 리스트,idx+1) 을 호출
from copy import deepcopy
def backtrack(arr,idx):
    array=[]
    array+=arr

    if idx<n1_len:
        backtrack(deepcopy(arr),idx+1)
        #print(array,idx)
        array.append(n1_array[idx])
        if len(array) == 6:
            result.append(array)
            return 0
        else:
            backtrack(array,idx+1)
    else:
        return -1

while True:
    result = []
    n1_array= list(map(int,input().split()))

    n1_len = n1_array.pop(0)

    if n1_len == 0:
        break

    else:
        backtrack([],0)
    result.sort()
    for i in result:
        print(" ".join(map(str,i)))
    print("")

