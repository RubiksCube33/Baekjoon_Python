w=0
for i in range(8):
    lst=input()
    for j in range(8):
        if lst[j] == "F":
            if i%2==0 and j%2==0:
                w+=1
            elif i%2==1 and j%2==1:
                w+=1
print(w)