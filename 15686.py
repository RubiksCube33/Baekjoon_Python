from itertools import combinations

N, M = map(int, input().split())

mapList = []
chickenShopList = []
homeList = []

shortestDistance = 9999999

for i in range(0, N):
    mapList.append(input().split())

for i in range(0, N):
    for j in range(0, N):
        if (mapList[i][j] == "2"):
            chickenShopList.append([j, i])
        elif (mapList[i][j] == "1"):
            homeList.append([j, i])

combinedChickenShop = list(combinations(chickenShopList, M))
chickenDistance = [0 for i in range(len(combinedChickenShop))]

for k in range(0, len(combinedChickenShop)):
    tempDistance = 0
    temp = 0
    for j in range(0, len(homeList)):
        tempShortest = 99999999
        for i in range(0, len(combinedChickenShop[0])):
            temp = abs(combinedChickenShop[k][i][0] - homeList[j][0]) + abs(
                combinedChickenShop[k][i][1] - homeList[j][1])
            if temp < tempShortest : tempShortest = temp
        tempDistance += tempShortest
        if tempDistance > shortestDistance: break
    if tempDistance < shortestDistance : shortestDistance = tempDistance

print(shortestDistance)