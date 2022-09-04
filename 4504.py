n=int(input())
while(1):
    p = int(input())
    if p == 0 : break
    if p % n == 0 : print(p,"is a multiple of",str(n)+'.')
    else : print(p,"is NOT a multiple of",str(n)+'.')