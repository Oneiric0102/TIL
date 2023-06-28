while True:
    curr = 0
    next = 1
    n = int(input())
    for i in range(0,n):
        sum = curr+next
        curr = next
        next = sum
    print(curr)