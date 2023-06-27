numbers = [1, 2, 3, 4, 5]
a = iter(numbers)

print(a)
print(next(a)) # 1
print(next(a)) # 2
print(next(a)) # 3
print(next(a)) # 4
print(next(a)) # 5
print(next(a)) # stop Error
