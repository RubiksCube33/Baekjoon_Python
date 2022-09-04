import sys
n = int(sys.stdin.readline())
lst = [list(map(int,sys.stdin.readline().split()))]
for i in range(1,n):
    lst[0][i] = max(lst[0][i],lst[0][i]+lst[0][i-1])
print(max(lst[0]))