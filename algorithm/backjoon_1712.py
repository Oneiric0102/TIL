import sys

A, B, C = map(int, sys.stdin.readline().split())

units = 0

if C <= B:
    units = -1
else:
    profit = C - B
    units = A // profit
    units += 1


print(units)
