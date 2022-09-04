n = int(input())
strlist = []
answer = []

for _ in range(n):
    strlist.append(input())

for i in range(0,len(strlist[0])):
    answer.append(strlist[0][i])
    for j in range(0,n):
        if(answer[i] != strlist[j][i]):
            answer[i] = "?"
print("".join(answer))