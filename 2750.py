N = int(input())
lst = []
for i in range(0,N):
    lst.append(int(input()))
lst.sort()
for i in range(0,len(lst)):
    print(lst[i])