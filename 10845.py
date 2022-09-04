#pypy3으로 제출
from collections import deque
import sys

n = int(input())
stack = deque([])
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stack.insert(len(stack),command[1])
    elif command[0] == "pop":
        if(len(stack)==0):print(-1)
        else:print(stack.popleft())
    elif command[0] == "size":print(len(stack))
    elif command[0] == "empty":
        if (len(stack) == 0):print(1)
        else:print(0)
    elif command[0] == "front":
        if (len(stack) == 0):
            print(-1)
        else:
            print(stack[0])
    elif command[0] == "back":
        if (len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])