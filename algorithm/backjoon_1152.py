import sys

line = sys.stdin.readline().strip()
words = 0

if line == "" or line == " ":
    print(0)

else:
    for i in range(len(line)):
        if line[i] == " " and i != 0 and i != len(line) - 1:
            words += 1

    print(words + 1)
