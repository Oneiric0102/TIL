import sys

A, B = sys.stdin.readline().split()

reversedA = ""
reversedB = ""

for i in reversed(A):
    reversedA += i

for i in reversed(B):
    reversedB += i

print(max(int(reversedA), int(reversedB)))
