a = input()
b = []
for i in range(len(a)):
    b.append(a[i])
b.sort()
b = list(reversed(b))
a = ""
for i in range(len(b)):
    a += b[i]
print(a)