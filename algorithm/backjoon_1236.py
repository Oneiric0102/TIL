import sys

N, M = map(int, sys.stdin.readline().split())
castle = []
answerX = 0
answerY = 0

for i in range(0, N):
    castle.append(sys.stdin.readline())

for i in castle:
    if "X" in i:
        continue
    else:
        answerX += 1

for i in range(M):
    isEmpty = True
    for j in range(N):
        if castle[j][i] == "X":
            isEmpty = False
            break
    if isEmpty:
        answerY += 1


print(max(answerX, answerY))
