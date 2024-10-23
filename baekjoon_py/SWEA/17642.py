
"""
두 변수에 저장된 값을 서로 같게 만들고자 한다.
두 변수를 같게 만들고자 조작할 수 있는데, 이 한 번의 조작은 두 종류의 연산 중 하나를 택하여 한 번 수행하는 것을 의미한다.
- A에 임의의 소수를 더한다
- B에 임의의 소수를 더한다.
"""
T= int(input())

for test_case in range(1,T+1):
    result = -1
    A,B = map(int,input().split())

    if A==B:
        result = 0
    elif B-A>1:
        dif = B-A
        # 두 수의 차이가 짝수
        if (dif)%2 ==0:
            result= dif//2

        # 두 수의 차이가 홀수
        elif (dif)%2 ==1:
            if dif ==3:
                result = 1
            elif dif>3:
                result = dif//2
    print("#%d %d" %(test_case, result))


