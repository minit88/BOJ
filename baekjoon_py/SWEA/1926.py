n = int(input())

result =""
for num in range(1,n+1):
    num_list = list(str(num))
    checked = 0
    cur_str = ""
    for n in num_list:
        if n in ["3","6","9"]:
            checked += 1
    if checked ==0:
        cur_str += "%d" %(num)

    elif checked >0:
        for i in range(checked):
            cur_str+= "%s" %("-")
    if (num != n):
        result +=cur_str
        result +=" "
    else:
        result +=cur_str
#result.remove
print(result)
