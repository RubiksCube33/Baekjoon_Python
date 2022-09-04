h,m = map(int,input().split())
time = (60 * h) + m
time -= 45
if time < 0 :
    time = 1440 + time

print(time//60,time%60)