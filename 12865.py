N, K = map(int, input().split())
backpack = [[0, 0]]
product = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    backpack.append(list(map(int, input().split())))

for i in range(1,N+1):
    for j in range(1,K+1):
        weight = backpack[i][0]
        value = backpack[i][1]

        if j < weight:
            product[i][j] = product[i-1][j]
        else:
            if value+product[i-1][j-weight] > product[i-1][j]:
                product[i][j] = value+product[i-1][j-weight]
            else : product[i][j] = product[i-1][j]

print(product[len(product)-1][len(product[1])-1])