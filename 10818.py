N = int(input())
lst = list(map(int,input().split()))
max = -1000001
min = 1000001
for i in range(0,N):
    if lst[i] > max : max = lst[i]
    if lst[i] < min : min = lst[i]
print(min,max)