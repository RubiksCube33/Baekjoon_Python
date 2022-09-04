N = int(input())
for i in range(N):
    inputstr = input()
    score = 0
    highscore = 0
    for j in range(len(inputstr)):
        if(inputstr[j] == "O"):
            score += 1
            highscore += score
        else :
            score = 0
    print(highscore)