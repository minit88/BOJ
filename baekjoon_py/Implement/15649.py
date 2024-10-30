from itertools import combinations, permutations

n, m = map(int, input().split())

a = [str(i) for i in range(1, n + 1)]


#for i in permutations(array,m):
#    print(" ".join(i))
def nm(array):
    #print(array)
    if len(array) == m:
        print(" ".join(array))

    else:
        for i in a:
            #print(i)
            if i not in array:
                nm(array + [i])


nm([])
