import sys
dm=set()
bm=set()
dbj=[]
n,m = map(int,sys.stdin.readline().split())
for i in range(n):
    dm.add(sys.stdin.readline())
for i in range(m):
    bm.add(sys.stdin.readline())
dbj = sorted(list(dm & bm))
print(len(dbj))
for i in range(len(dbj)):
    print(dbj[i],end="")