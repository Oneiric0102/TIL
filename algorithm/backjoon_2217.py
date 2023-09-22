import sys

rope_list = []
max_sum = 0
n = int(sys.stdin.readline())
for i in range(n):
    rope_list.append(int(sys.stdin.readline()))

rope_list.sort(reverse=True)
for i in range(len(rope_list)):
    max_sum = max((i + 1) * rope_list[i], max_sum)

print(max_sum)
