import sys

N, M = map(int, sys.stdin.readline().split())

basket = [i + 1 for i in range(N)]
for num in range(M):
    i, j = map(int, sys.stdin.readline().split())
    temp = basket[i - 1]
    basket[i - 1] = basket[j - 1]
    basket[j - 1] = temp
for i in basket:
    print(i, end=" ")
