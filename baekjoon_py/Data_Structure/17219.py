n,m = map(int,input().split())
password_arr = dict()
# n+2부터
for i in range(n):
    domain, password = map(str,input().split())

    password_arr[domain] = password
for i in range(m):
    print(password_arr[str(input())])
