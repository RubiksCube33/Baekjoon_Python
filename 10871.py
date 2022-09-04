N,X = map(int,input().split())
lst = list(map(int,input().split()))
ans = ""
for i in range(N):
    if(lst[i] < X):ans+=str(lst[i])+" "
print(ans)