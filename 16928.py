N,M = map(int,input().split())
ladderandSnake = []
length = 0
notArrived = True
gameboard = [i for i in range(101)]
visited = [False for i in range(101)]
visitedNum = [0 for i in range(101)]
bfsQueue = []
queueSize = 0
qlen = 0
route = []

for i in range(N+M):
    ladderandSnake.append(list(map(int,input().split())))
ladderandSnake.sort()

for i in range(len(ladderandSnake)):
    visited[ladderandSnake[i][1]] = False

for i in range(len(ladderandSnake)):
    gameboard[ladderandSnake[i][0]] = ladderandSnake[i][1]

bfsQueue.append(gameboard[1])
queueSize = len(bfsQueue)

while(bfsQueue):
    temp = bfsQueue.pop(0)
    if temp == 100:
        print(visitedNum[100])
        break
    for i in range(1,7):
        move = temp + i
        if move <= 100:
            if gameboard[move] != move:
                move = gameboard[move]
        if move <= 100 and visited[move] == False:
            visited[move] = True
            visitedNum[move] = visitedNum[temp] + 1
            bfsQueue.append(move)