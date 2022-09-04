N = int(input())
lst = []
for i in range(N):
    lst.append(input().split())
    lst[i][0] = int(lst[i][0])
lst.sort(key=lambda x:(x[0]))

for i in range(N):
    print(lst[i][0],lst[i][1])