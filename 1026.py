import sys
n = int(sys.stdin.readline())
lst1 = list(map(int,sys.stdin.readline().split()))
lst2 = list(map(int,sys.stdin.readline().split()))

lst1.sort()
lst2.sort()
a = 0

for i in range(n):
    a += lst1[i]*lst2[n-i-1]
print(a)