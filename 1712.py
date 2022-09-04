A,B,C = map(int,input().split())
revenue = C - B
if revenue <= 0 : print(-1)
else:
    print(A//revenue + 1)