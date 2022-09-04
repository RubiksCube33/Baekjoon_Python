n = int(input())
lst = list(map(int,input().split()))
top = 0
for i in range(len(lst)):
    if lst[i] > top:
        top = lst[i]

for i in range(len(lst)):
    lst[i] = (lst[i]/top)*100

print(sum(lst)/n)