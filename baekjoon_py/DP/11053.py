n= int(input())

array = list(map(int,input().split()))
num_array_length = [ 0 for _ in range(1001)] # 1~ 1000까지 자신의 수까지 가장 큰 수열의 길이 저장

result = 1

for i in range(n):

    cur_num = array[i]
    cur_length = 1
    pre_max_length = 0
    for num in range(1,cur_num):
        pre_max_length = max(num_array_length[num],pre_max_length)
    cur_length += pre_max_length
    num_array_length[cur_num] = max(num_array_length[cur_num],cur_length)

result = max(num_array_length)

print(result)




