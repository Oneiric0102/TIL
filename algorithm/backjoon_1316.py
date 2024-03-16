import sys

N = int(sys.stdin.readline())

group_word_count = 0

for i in range(N):
    line = sys.stdin.readline().strip()
    before_char = ""
    before_char_list = []
    is_group_word = True
    for char in line:
        if before_char != char:
            if char in before_char_list:
                is_group_word = False
                break
            else:
                before_char = char
                before_char_list.append(char)

    if is_group_word:
        group_word_count += 1

print(group_word_count)
