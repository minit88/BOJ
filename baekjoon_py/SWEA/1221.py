
T = int(input())

num_str_array = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for test_case in range(1,T+1):
    test_caseAndLen = str(input())

    input_str_array = list(map(str,input().split()))
    result_num_array = []
    result_str_array = []

    for input_str in input_str_array:
        for num_str_idx,num_str in enumerate(num_str_array):
            if input_str == num_str:
                result_num_array.append(num_str_idx)

    result_num_array.sort()

    for result_num in result_num_array:
        result_str_array.append(num_str_array[result_num])
    print("#%d" %test_case)
    print("%s" %(" ".join(map(str,result_str_array))))