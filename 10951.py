while(1):
    try : a,b=map(int,input().split())
    except : break
    if 0 > a or b > 10 : break
    print(a+b)