import sys
n=int(sys.stdin.readline())
for _ in range(0,n):
    a, b, c = map(int, sys.stdin.readline().split(":"))
    a = bin(a)[2:]
    b = bin(b)[2:]
    c = bin(c)[2:]
    while (len(a) < 6):
        a = "0" + a
    while (len(b) < 6):
        b = "0" + b
    while (len(c) < 6):
        c = "0" + c
    res=""
    for i in range(0,6):
        res+=a[i]+b[i]+c[i]
    print(res,a+b+c)
