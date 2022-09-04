from collections import deque
import sys

def fact(num):
    ans = 1
    for i in range(1,num+1):
        ans *= i
    return ans


n = int(sys.stdin.readline())
factstr = str(fact(n))
index = 0
for i in range(len(factstr)-1,-1,-1):
    if(factstr[i]=="0"):index+=1
    else:break
print(index)