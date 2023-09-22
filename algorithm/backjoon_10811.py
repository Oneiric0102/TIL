import sys

N, M = map(int, sys.stdin.readline().split())

basket = [i + 1 for i in range(N)]
for num in range(M):
    i, j = map(int, sys.stdin.readline().split())
    basket = basket[: i - 1] + list(reversed(basket[i - 1 : j])) + basket[j:]
for i in basket:
    print(i, end=" ")
