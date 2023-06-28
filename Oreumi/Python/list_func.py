a = [1,2,3]
a.append(4)
a.append(5)

print(a)

a = []
for i in range(1,6):
    a.append(i)

print(a)

for i in range(1,6):
    a.remove(i)
print(a)

for i in range(1,6):
    a.append(i)

print(a.pop(3))
print(a)

a = [5, 3, 2, 4, 6, 1]
a.sort(reverse=True)
print(a)

a = [1,2,3,4,5,6]
print(a[3:5])

a = [1,2,3,4,5,6]
b = a
print(b)

a = [i**2 for i in range(1,6)]

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

a= a + b
print(a)

a = a*3
print(a)

a.insert(1,"4")
print(a)

index = a.index("1")
print(index)
print(len(a))

print(a.count("2"))
a.reverse()
print(a)

n = int(input())
a = [1,2,3]
