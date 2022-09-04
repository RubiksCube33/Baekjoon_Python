import sys
n=int(sys.stdin.readline())
lst=[float(sys.stdin.readline()) for _ in range(n)]
for i in range(1,n-1):
    lst[i] = max(lst[i],lst[i]*lst[i-1])
print("{:.3f}".format(max(lst)))