diceTop = 0
diceLeft = 0
diceRight = 0
diceFront = 0
diceBack = 0
diceBottom = 0

mapList = []

n,m,y,x,k = map(int,input().split())
for i in range(0,n):
    mapList.append(input().split())

movingList = (input().split())

for i in range(0,len(movingList)):
    direction = int(movingList[i])
    if direction == 1:
        if x+1 >= len(mapList[0]):
            continue
        x += 1
    elif direction == 2:
        if x-1 < 0 :
            continue
        x -= 1
    elif direction == 3:
        if y - 1 < 0:
            continue
        y -= 1
    elif direction == 4:
        if y + 1 >= len(mapList):
            continue
        y += 1

    temp = diceTop

    if direction == 1:
        diceTop = diceLeft
        diceLeft = diceBottom
        diceBottom = diceRight
        diceRight = temp
    elif direction == 2:
        diceTop = diceRight
        diceRight = diceBottom
        diceBottom = diceLeft
        diceLeft = temp
    elif direction == 3:
        diceTop = diceFront
        diceFront = diceBottom
        diceBottom = diceBack
        diceBack = temp
    elif direction == 4:
        diceTop = diceBack
        diceBack = diceBottom
        diceBottom = diceFront
        diceFront = temp

    if(mapList[y][x] == "0"):
        mapList[y][x] = str(diceBottom)
    else :
        diceBottom = int(mapList[y][x])
        mapList[y][x] = "0"
    print(diceTop)
