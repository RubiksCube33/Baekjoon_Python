h,m=map(int,input().split())
m+=int(input())
h+=m//60
m=m%60
if h>=24:
  h=h%24
print(h,m)