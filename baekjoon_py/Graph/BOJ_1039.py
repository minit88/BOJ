
from collections import deque
from copy import deepcopy


# 숫자 리스트를 정수로 변환
def list_to_int(array):
    cur_num=""
    for i in array:
        cur_num+=str(i)
    return int(cur_num)

# idx 두개를 입력 받아 서로 바꾸기
def num_changer(num_array,idx1,idx2):
    num_idx1 = num_array[idx1]
    num_idx2 = num_array[idx2]

    num_array[idx1] = num_idx2
    num_array[idx2] = num_idx1

    return num_array

def is_possbile_change(num_array):
    array_in_def = deepcopy(num_array)
    count_zero = 0
    for i in range(len(num_array)):
        if array_in_def[i] ==0:
            count_zero+=1
    if (len(array_in_def) - count_zero )>1 or len(num_array)>=3:
        return True
    else:
        return False

n,c = map(str,input().split())

n= list(n)
c= int(c)
for i in range(len(n)):
    n.append(int(n.pop(0)))

q = deque([])
result = -1

copied_n = deepcopy(n)
copied_n.sort()
copied_n.reverse()

# 현재 리스트 중에서 만들 수 있는 최대값
max_array_num = list_to_int(copied_n)

# 1자리수이면 그냥 출력
if len(n) != 1:
    if is_possbile_change(n):
        q.append((n,0))
    elif is_possbile_change(n):
        pass
elif len(n) == 1:
    pass

while q:

    num_array, count = q.popleft()

    if count == c:
        result = max(result,list_to_int(num_array))
        continue

    # 각 자리 돌면서 자기 보다 큰거 찾기
    for i in range(len(num_array)):
        max_num = max(num_array[i:])

        # 뒷자리 수 중에 자신보다 큰 수가 존재할 경우 바꿔줘야함.
        if num_array[i]<max_num:
            for j in range(i+1,len(num_array)):
                if num_array[j] == max_num and max_num != num_array[i]:

                    changed_array = num_changer(deepcopy(num_array),i,j)

                    q.append((changed_array,count+1))

        # 현재 수가 가장 최대값일 경우 == 바꿀 수가 없는 경우
        elif i == len(num_array)-1 and list_to_int(num_array) == max_array_num :

            # 남은 카운트가 짝수이면 그대로 출력
            if (c-count) %2 ==0:
                result = max_array_num
                q.clear()
                break

            # 남은 카운트가 홀수이면 뒤에 두개를 바꾸기 -> 같은 수가 존재하면 안바꿔도 됨 (AA->AA)
            elif (c-count) %2 ==1:
                if len(set(num_array)) != len(num_array):
                    result = max_array_num
                else:
                    changed_array = num_changer(num_array,len(n)-2,len(n)-1)
                    result = max(result,list_to_int(changed_array))
                q.clear()
                break


print(result)




