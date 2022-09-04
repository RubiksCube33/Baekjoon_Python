n = int(input())

for i in range(n):
    lst0 = [1,0]
    lst1 = [0,1]
    temp = int(input())

    if temp == 0:
        print(1,0)
        continue

    if temp == 1:
        print(0,1)
        continue

    for i in range(2,temp+1):
        lst0.append(lst0[i-1] + lst0[i-2])
        lst1.append(lst1[i-1] + lst1[i-2])

    print(lst0[-1],lst1[-1])