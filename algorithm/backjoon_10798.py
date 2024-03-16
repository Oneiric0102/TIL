import sys

lines = []
answer = ""

for i in range(5):
    line = sys.stdin.readline().strip()
    lines.append(line)

for i in range(15):
    temp = ""
    for j in range(5):
        if len(lines[j]) <= i:
            continue
        else:
            temp += lines[j][i]

    if temp == "":
        break
    else:
        answer += temp

print(answer)
