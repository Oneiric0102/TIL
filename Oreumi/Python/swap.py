a = [1, 2, 3, 4, 5]
for i in range(0,len(a)//2):
    temp = a[i]
    a[i] = a[len(a)-i-1]
    a[len(a)-i-1] = temp

print(a)