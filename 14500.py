import sys

n, m = map(int, input().split())
boardlst = []
largest = 0
tempsum = 0

for _ in range(n):
    boardlst.append(list(map(int, sys.stdin.readline().split())))

for i in range(n - 1):  # ㅜ
    for j in range(1, m - 1):
        tempsum = boardlst[i][j - 1] + boardlst[i][j] + boardlst[i][j + 1] + boardlst[i + 1][j]
        if tempsum > largest: largest = tempsum

for i in range(n - 2):  # ㅏ
    for j in range(0, m - 1):
        tempsum = boardlst[i][j] + boardlst[i + 1][j] + boardlst[i + 2][j] + boardlst[i + 1][j + 1]
        if tempsum > largest: largest = tempsum

for i in range(n - 2):  # ㅓ
    for j in range(1, m):
        tempsum = boardlst[i][j] + boardlst[i + 1][j] + boardlst[i + 2][j] + boardlst[i + 1][j - 1]
        if tempsum > largest: largest = tempsum

for i in range(1, n):  # ㅗ
    for j in range(0, m - 2):
        tempsum = boardlst[i][j] + boardlst[i][j + 1] + boardlst[i][j + 2] + boardlst[i - 1][j + 1]
        if tempsum > largest: largest = tempsum

for i in range(n):  # ㅡ
    for j in range(m - 3):
        tempsum = boardlst[i][j] + boardlst[i][j + 1] + boardlst[i][j + 2] + boardlst[i][j + 3]
        if tempsum > largest: largest = tempsum

for i in range(n - 3):  # ㅣ
    for j in range(m):
        tempsum = boardlst[i][j] + boardlst[i + 1][j] + boardlst[i + 2][j] + boardlst[i + 3][j]
        if tempsum > largest: largest = tempsum

for i in range(0, n - 1):  # ㄱㄴ
    for j in range(m - 2):
        tempsum = boardlst[i][j] + boardlst[i][j + 1] + boardlst[i + 1][j + 1] + boardlst[i + 1][j + 2]
        if tempsum > largest: largest = tempsum

for i in range(1, n):  # ㄱㄴ 좌우반전
    for j in range(m - 2):
        tempsum = boardlst[i][j] + boardlst[i][j + 1] + boardlst[i - 1][j + 1] + boardlst[i - 1][j + 2]
        if tempsum > largest: largest = tempsum

for i in range(0, n - 2):  # 늑
    for j in range(m - 1):
        tempsum = boardlst[i][j] + boardlst[i + 1][j] + boardlst[i + 1][j + 1] + boardlst[i + 2][j + 1]
        if tempsum > largest: largest = tempsum

for i in range(0, n - 2):  # 늑 좌우반전
    for j in range(1, m - 1):
        tempsum = boardlst[i][j] + boardlst[i + 1][j] + boardlst[i + 1][j - 1] + boardlst[i + 2][j - 1]
        if tempsum > largest: largest = tempsum

for i in range(0, n - 2):  # L
    for j in range(0, m - 1):
        tempsum = boardlst[i][j] + boardlst[i + 1][j] + boardlst[i + 2][j] + boardlst[i + 2][j + 1]
        if tempsum > largest: largest = tempsum

for i in range(0, n - 2):  # L 좌우반전
    for j in range(1, m):
        tempsum = boardlst[i][j] + boardlst[i + 1][j] + boardlst[i + 2][j] + boardlst[i + 2][j - 1]
        if tempsum > largest: largest = tempsum

for i in range(0, n - 1):  # ㄴ
    for j in range(0, m - 2):
        tempsum = boardlst[i][j] + boardlst[i + 1][j] + boardlst[i + 1][j + 1] + boardlst[i + 1][j + 2]
        if tempsum > largest: largest = tempsum

for i in range(1, n):  # ㄴ 좌우반전
    for j in range(0, m - 2):
        tempsum = boardlst[i][j] + boardlst[i][j + 1] + boardlst[i][j + 2] + boardlst[i - 1][j + 2]
        if tempsum > largest: largest = tempsum

for i in range(0, n - 1):  # ㄱ 인데 가로로 긴거
    for j in range(0, m - 2):
        tempsum = boardlst[i][j] + boardlst[i][j + 1] + boardlst[i][j + 2] + boardlst[i + 1][j + 2]
        if tempsum > largest: largest = tempsum

for i in range(0, n - 2):  # ㄱ 인데 세로로 긴거
    for j in range(0, m - 1):
        tempsum = boardlst[i][j] + boardlst[i][j + 1] + boardlst[i + 1][j + 1] + boardlst[i + 2][j + 1]
        if tempsum > largest: largest = tempsum

for i in range(0, n - 1):  # ㄱ 인데 가로로 긴거 좌우반전
    for j in range(0, m - 2):
        tempsum = boardlst[i][j] + boardlst[i][j + 1] + boardlst[i][j + 2] + boardlst[i + 1][j]
        if tempsum > largest: largest = tempsum

for i in range(0, n - 2):  # ㄱ 인데 세로로 긴거 좌우반전
    for j in range(0, m - 1):
        tempsum = boardlst[i][j] + boardlst[i][j + 1] + boardlst[i + 1][j] + boardlst[i + 2][j]
        if tempsum > largest: largest = tempsum

for i in range(0, n - 1):  # ㄱ 인데 세로로 긴거 좌우반전
    for j in range(0, m - 1):
        tempsum = boardlst[i][j] + boardlst[i][j + 1] + boardlst[i + 1][j] + boardlst[i + 1][j + 1]
        if tempsum > largest: largest = tempsum

print(largest)