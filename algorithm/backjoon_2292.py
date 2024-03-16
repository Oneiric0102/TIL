import sys

n = int(sys.stdin.readline())
result = 0
compare = 1

while compare < n:
    result += 1
    compare += result * 6

print(result + 1)
