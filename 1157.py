str = input().lower()
mostused = "0"
mostusednum = 0
arr = [0 for i in range(26)]

for i in range(0,len(str)):
    arr[ord(str[i])-97] += 1

for j in range(0,26):
    if arr[j] > mostusednum :
        mostused = chr(j+65)
        mostusednum = arr[j]
    elif arr[j] == mostusednum :
        mostused = "?"

print(mostused)