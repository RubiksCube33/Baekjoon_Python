lst = []
for _ in range(int(input())):
    temp = int(input())
    if temp == 0:
        lst.pop(-1)
        continue
    lst.append(temp)
print(sum(lst))