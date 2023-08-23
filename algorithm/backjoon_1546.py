import sys

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
max_score = max(score)
sum = 0

for i in score:
    i = i / max_score * 100
    sum += i

print(sum / N)
