n,m=map(int,input().split())
lst = [1 for _ in range (m)]
for i in range(n**m):
    for j in range(m-1,0,-1):
        if(lst[j] > n):
            lst[j-1] += 1
            lst[j] = 1
    for k in range(m):
        print(lst[k],end=" ")
    print()
    lst[m-1] += 1