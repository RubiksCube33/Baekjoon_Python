import sys
n=int(sys.stdin.readline())
result=0
for _ in range(n-1):
    result+=int(sys.stdin.readline())-1
print(result+int(sys.stdin.readline()))