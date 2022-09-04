a = int(input())
b = int(input())

first = a * (b % 10)
second = (a * (b % 100 - b % 10) // 10)
thrid = a * (b // 100)

print(first)
print(second)
print(thrid)
print(a*b)