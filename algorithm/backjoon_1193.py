import sys

x = int(sys.stdin.readline())

n = 1
compare = 1
reverse = True
if x == 1:
    print("1/1")
else:
    while x > compare:
        n += 1
        reverse = not reverse
        if compare + n >= x:
            break
        else:
            compare += n

    num = x - compare
    if not reverse:
        denominator = n - num + 1
        numerator = 1 + num - 1
    else:
        denominator = 1 + num - 1
        numerator = n - num + 1

    print(str(numerator) + "/" + str(denominator))
