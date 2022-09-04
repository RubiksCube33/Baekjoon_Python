ans = [-1 for _ in range(26)]
str1 = input()
for i in range(0,len(str1)):
    if(ans[int(ord(str1[i]))-97] == -1):
        ans[int(ord(str1[i])) - 97] = i
anstr = ""
for i in range(0,26):
    anstr += (str(ans[i]) + " ")
print(anstr)