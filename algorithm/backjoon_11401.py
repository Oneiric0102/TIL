import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[-1 for i in range(0, K + 1)] for j in range(0, N + 1)]


def bino_coef(n, k):
    if k > n or n == 0:
        dp[n][k] = 0

    if k == n or k == 0:
        dp[n][k] = 1

    if dp[n][k] == -1:
        dp[n][k] = bino_coef(n - 1, k) + bino_coef(n - 1, k - 1)

    return dp[n][k]


print(bino_coef(N, K))
