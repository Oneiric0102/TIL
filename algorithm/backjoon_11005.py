import sys

N, B = map(int, sys.stdin.readline().split())
number = dict(zip(range(36), "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"))


answer = ""

while N >= B:
    answer = number[N % B] + answer
    N = N // B

if N != 0:
    answer = number[N] + answer

print(answer)
