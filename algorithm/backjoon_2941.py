import sys

line = sys.stdin.readline().strip()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in range(0, len(croatia)):
    line = line.replace(croatia[i], str(i))

print(len(line))
