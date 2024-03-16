import sys

n = int(sys.stdin.readline())

result = 2
for i in range(0, n):
    result = result * 2 - 1

print(result**2)
