a = int(input())
bina = bin(a)
bina = bina[2:]
a = 0
for i in range(len(bina)):
    if(bina[i] == "1"):
        a+=1
print(a)