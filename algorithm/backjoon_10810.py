import sys

N, M = map(int, sys.stdin.readline().split())

basket = [0 for _ in range(N)]
for i in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for num in range(i - 1, j):
        basket[num] = k

for i in basket:
    print(i, end=" ")
