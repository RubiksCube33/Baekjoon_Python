import copy

def swap(gameboard,pivotStart,pivotEnd):
    for i in range(0, int((pivotEnd - pivotStart + 1) // 2)):
        temp = gameboard[pivotStart+i]
        gameboard[pivotStart+i] = gameboard[pivotEnd-i]
        gameboard[pivotEnd-i] = temp
    return gameboard

def findFront(gameboard):
    pivotStart = 1
    pivotEnd = 1
    start = False
    for i in range(1, len(gameboard)):
        if gameboard[i] != i and start == False:
            pivotStart = i
            start = True
        if i > 1 and gameboard[i] == pivotStart:
            pivotEnd = i
            break

    return pivotStart,pivotEnd

def findBack(gameboard):
    pivotStart = 1
    pivotEnd = 1
    start = False

    for i in range(len(gameboard) - 1, -1, -1):
        if gameboard[i] != i and start == False:
            pivotEnd = i
            start = True
        if i < len(gameboard)-1 and gameboard[i] == pivotEnd :
            pivotStart = i
            break

    return pivotStart,pivotEnd

N = int(input())
gameboard_original = [0]+list(map(int,input().split()))
gameboard = copy.deepcopy(gameboard_original)

pivotstart_1 = 1
pivotstart_2 = 1
pivotend_1 = 1
pivotend_2 = 1

pivotstart_1, pivotend_1 = findFront(gameboard)
swap(gameboard,pivotstart_1,pivotend_1)

pivotstart_2, pivotend_2 = findFront(gameboard)
swap(gameboard,pivotstart_2,pivotend_2)

error = False
for i in range(1,len(gameboard)):
    if gameboard[i] != i:
        error = True

if error == False:
    print(pivotstart_1, pivotend_1)
    print(pivotstart_2, pivotend_2)
else:
    gameboard = copy.deepcopy(gameboard_original)

    pivotstart_1 = 1
    pivotstart_2 = 1
    pivotend_1 = 1
    pivotend_2 = 1

    pivotstart_1, pivotend_1 = findBack(gameboard)
    swap(gameboard, pivotstart_1, pivotend_1)

    pivotstart_2, pivotend_2 = findBack(gameboard)
    swap(gameboard, pivotstart_2, pivotend_2)

    print(pivotstart_1, pivotend_1)
    print(pivotstart_2, pivotend_2)