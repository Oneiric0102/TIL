import sys

n = int(sys.stdin.readline())


def decording(letter):
    root = int(len(letter) ** (1 / 2))
    result = ""

    for i in range(root - 1, -1, -1):
        for j in range(0, root):
            result += letter[j * root + i]
    return result


for i in range(0, n):
    letter = sys.stdin.readline()
    print(decording(letter))
