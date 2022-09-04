n = int(input())
for i in range(n):
    ans = ""
    inputValue = input().split()
    for j in range(len(inputValue[1])):
        ans += inputValue[1][j] * int(inputValue[0])
    print(ans)