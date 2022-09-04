import sys
n=int(sys.stdin.readline())
for _ in range(0,n):
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str=sys.stdin.readline()
    sol=sys.stdin.readline()
    dic={" ":" "}
    for i in range(len(sol)-1):
        dic[abc[i]]=sol[i]
    for i in range(len(str)-1):
        print(dic[str[i]],end="")
    print()