from itertools import combinations

input_array = list(str(input()))
stack =[]
set_array = []
for i in range(len(input_array)):
    if input_array[i] == "(":
        stack.append(i)

    elif input_array[i] == ")":
        idx = stack.pop(-1)
        set_array.append((idx,i)) # (_idx, )_idx
results = set()
for c in range(1,len(set_array)+1):
    num_list = combinations(set_array,c)

    for j in num_list :
        removed_idx = []
        result = ""
        for i in j:
            idx1, idx2 = i
            removed_idx.append(idx1)
            removed_idx.append(idx2)

        for i in range(len(input_array)):
            if i in removed_idx:
                continue
            else:
                result += input_array[i]
        results.add(result)
results = sorted(results)

for i in results:
    print(i)







