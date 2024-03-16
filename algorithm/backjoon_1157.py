import sys

str = sys.stdin.readline().strip()
char_count = {}

for char in str:
    char_alpha = char.upper()
    if char_alpha in char_count:
        char_count[char_alpha] += 1
    else:
        char_count[char_alpha] = 1

char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

if len(char_count) == 1:
    print(char_count[0][0])
elif char_count[0][1] == char_count[1][1]:
    print("?")
else:
    print(char_count[0][0])
