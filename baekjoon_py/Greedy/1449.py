n,m = map(int,input().split())

array =[0 for i in range(1001)]

input_array = list(map(int,input().split()))

input_array.sort()
count = 0
for i in input_array:

    if array[i]==0:
        start_idx = i
        end_idx = i+m
        if end_idx >= 1000:
            end_idx = 1001

        for idx in range(start_idx,end_idx):
            array[idx] += 1
        count+=1

    elif array[i] == 1:
        continue
#print(array[1:100])
print(count)
