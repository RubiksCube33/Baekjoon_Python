import heapq
import sys

median_up = []
median_down = []

N = int(sys.stdin.readline())
heapq.heappush(median_down,-(int(sys.stdin.readline())))

print(-median_down[0])

if N >= 2:
    temp = int(sys.stdin.readline())
    median_down_top = -heapq.heappop(median_down)

    if median_down_top > temp:
        heapq.heappush(median_up, median_down_top)
        heapq.heappush(median_down, -temp)
    else:
        heapq.heappush(median_up, temp)
        heapq.heappush(median_down, -median_down_top)

    print(-median_down[0])

for _ in range(N-2):
    temp = int(sys.stdin.readline())
    median_down_top = -median_down[0]
    median_up_bot = median_up[0]

    if median_down_top < temp:
        if(len(median_down) > len(median_up)):
            heapq.heappush(median_up, temp)
        else:
            if median_up_bot < temp:
                heapq.heappush(median_down, -heapq.heappop(median_up))
                heapq.heappush(median_up,temp)
            else:
                heapq.heappush(median_down,-temp)
    else:
        if (len(median_down) > len(median_up)):
            heapq.heappush(median_up, -heapq.heappop(median_down))
            heapq.heappush(median_down, -temp)
        else:
            heapq.heappush(median_down, -temp)
    print(-median_down[0])