import sys

S = sys.stdin.readline()

count0 = 0
count1 = 0

for i in S:
    if i == "0":
        count0 += 1
    elif i == "1":
        count1 += 1

while count0 > 0:
    for i in range(len(S) - 1, -1, -1):
        if S[i] == "0":
            S = S[:i] + S[i + 1 :]
            count0 -= 2
            break

S = S.replace("1", "", int(count1 / 2))

print(S)
