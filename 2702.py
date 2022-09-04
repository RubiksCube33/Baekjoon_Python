#pypy3으로 제출
import sys
n=int(sys.stdin.readline())
q=0
w=0
e=0
for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())
    if a<b:
        e=a
        a=b
        b=e
    e=a
    while(1):
        if e%a==0 and e%b==0:
            q=e
            break
        e+=1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            w=i
    print(q,w)