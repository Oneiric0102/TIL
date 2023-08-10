import sys

attend = [False for i in range(0, 31)]

for i in range(0, 28):
    num = int(sys.stdin.readline())
    attend[num] = True

for i in range(1, len(attend)):
    if not attend[i]:
        print(i)
