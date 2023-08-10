import sys

n = int(sys.stdin.readline())
paper = []
isdone = []

for i in range(0, n):
    paper.append(list(map(int, sys.stdin.readline().split())))
    isdone.append([False for i in range(0, n)])

divide = 1
done_sum = 0
white = 0
blue = 0

while done_sum < n * n:
    side_length = int(n / divide)
    for i in range(0, divide):
        for j in range(0, divide):
            if isdone[i * side_length][j * side_length] == True:
                continue
            color = paper[i * side_length][j * side_length]
            is_break = False
            for k in range(i * side_length, (i + 1) * side_length):
                for l in range(j * side_length, (j + 1) * side_length):
                    if paper[k][l] != color:
                        is_break = True
                        break
                if is_break:
                    break

            if not is_break:
                for k in range(i * side_length, (i + 1) * side_length):
                    for l in range(j * side_length, (j + 1) * side_length):
                        isdone[k][l] = True
                        done_sum += 1

                if color == 0:
                    white += 1
                else:
                    blue += 1
    divide *= 2


print(white)
print(blue)
