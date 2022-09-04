import sys

def fact(num):
    if(num == 0):return 1
    else:num=num*fact(num-1)
    return num

n = int(sys.stdin.readline())
print(fact(n))