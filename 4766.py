i=float(input())
j=float(input())
print("{:.2f}".format(j-i))
while(True):
    i=j
    j=float(input())
    if j==999:break
    print("{:.2f}".format(j-i))