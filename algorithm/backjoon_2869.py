import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

h = 0
day = 0
if A >= V:
    print(1)
else:
    min_height = V - A
    print(math.ceil(min_height / (A - B) + 1))
