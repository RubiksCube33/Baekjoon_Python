from collections import Counter
import sys

n=int(input())
lst=[]
for i in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()
mode = Counter(lst).most_common()

print(round(sum(lst)/n))
print(lst[n//2])
if len(mode) > 1:
    if mode[0][1] == mode[1][1]:print(mode[1][0])
    else:print(mode[0][0])
else:print(mode[0][0])
print(lst[n-1]-lst[0])