import sys

chess = []
white = 0
for i in range(8):
    chess.append(sys.stdin.readline())

for i in range(0, 8):
    for j in range(i % 2, 8, 2):
        if chess[i][j] == "F":
            white += 1

print(white)
