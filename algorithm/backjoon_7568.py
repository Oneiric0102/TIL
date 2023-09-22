import sys

N = int(sys.stdin.readline())

person = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    person.append((x, y))

rate = [0 for i in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if person[i][0] > person[j][0] and person[i][1] > person[j][1]:
            rate[j] += 1
        elif person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            rate[i] += 1

for r in rate:
    print(r + 1, end=" ")
