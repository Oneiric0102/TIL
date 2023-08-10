import sys

n = int(sys.stdin.readline())
observe = []
count = 0

for i in range(0, n):
    observe.append(list(map(int, sys.stdin.readline().split())))

cow_location = [-1 for _ in range(0, 10)]

for move in observe:
    if cow_location[move[0] - 1] == -1:
        cow_location[move[0] - 1] = move[1]
    elif cow_location[move[0] - 1] == move[1]:
        continue
    else:
        cow_location[move[0] - 1] = move[1]
        count += 1

print(count)
