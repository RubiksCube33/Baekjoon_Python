A = int(input())
B = int(input())
C = int(input())
res = str(A*B*C)
anslist = [0 for _ in range(0,10)]

for i in range(0,10):
    for j in range(0,len(res)):
        if(res[j] == str(i)):
            anslist[i] += 1
    print(anslist[i])