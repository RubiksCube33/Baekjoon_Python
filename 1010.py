from math import comb
a = int(input())
for i in range(a):
    r,n = map(int,input().split())
    print(comb(n,r))