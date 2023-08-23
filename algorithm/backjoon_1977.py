import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
sum = 0

start = M ** (1 / 2)
end = N ** (1 / 2)

if start.is_integer():
    start = int(start)
else:
    start = int(start) + 1

end = int(end) + 1

min = start**2
for i in range(start, end):
    sum += i**2

if not sum:
    print(-1)
else:
    print(sum)
    print(min)
