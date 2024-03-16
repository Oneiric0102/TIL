import sys

str = sys.stdin.readline().strip()

isPallindrom = 1
for i in range(len(str) // 2):
    if str[i] != str[len(str) - 1 - i]:
        isPallindrom = 0
        break

print(isPallindrom)
