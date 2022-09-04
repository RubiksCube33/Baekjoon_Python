lst = []
for i in range(0,10):
    lst.append(int(input()))
anslst = []
anslst.append(lst[0]%42)
for i in range(1,10):
    for j in range(0,len(anslst)):
        if(lst[i] % 42 == anslst[j]):
            break
        if j == len(anslst)-1:anslst.append(lst[i]%42)
print(len(anslst))