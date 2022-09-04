import sys
n=int(sys.stdin.readline())
lst=[sys.stdin.readline() for _ in range(n)]
garo = 0
sero = 0
index = 0
index_sero = 0

for i in range(0,n):
    for j in range(0,n):
        if lst[i][j] == ".":index += 1
        else :
            if index >= 2 : garo += 1
            index = 0
        if lst[j][i] == ".":index_sero += 1
        else :
            if index_sero >= 2 : sero += 1
            index_sero = 0
    if index >= 2 : garo += 1
    if index_sero >= 2 : sero += 1
    index = 0
    index_sero = 0
print(garo,sero)