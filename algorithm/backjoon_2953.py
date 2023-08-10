import sys

rate = []
for i in range(0, 5):
    rate.append(list(map(int, sys.stdin.readline().split())))

total_rate = [0, 0, 0, 0, 0]

for i in range(0, len(rate)):
    for score in rate[i]:
        total_rate[i] += score

print(total_rate.index(max(total_rate)) + 1, end=" ")
print(max(total_rate))
