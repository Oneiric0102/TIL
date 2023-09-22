import sys

N, K = map(int, sys.stdin.readline().split())

arr = [i for i in range(1, N + 1)]
answer = []

idx = 0

while arr:
    idx = (idx + K - 1) % len(arr)
    answer.append(arr.pop(idx))

print("<", end="")
print(", ".join(str(i) for i in answer), end="")
print(">")
