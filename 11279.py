import heapq
import sys

n = int(input())
lst = []

for _ in range(n):
    temp = int(sys.stdin.readline())
    if temp == 0:
        try:
            print(-(heapq.heappop(lst)))
        except:
            print(0)
    else:
        heapq.heappush(lst, (-temp))