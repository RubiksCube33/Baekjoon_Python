n=int(input())
if n==1:print("*")
else:
    for i in range(1,n+1):
        for j in range(1, n * 2 + 1):
            if i % 2 == 1:
                if j % 2 == 0:
                    print(" ", end="")
                else:
                    print("*", end="")
            else:
                if j % 2 == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()