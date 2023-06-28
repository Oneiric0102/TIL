numbers = [1,2,2,3,3,5]
set_numbers = set(numbers)
print(len(set_numbers))

a = {1,2,3,5}
b = {4,5,6,7}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(a-b)
print(a&b)
print(a|b)

a.add(4)
print(a)
a.remove(5)
a.discard(5)
print(a)

a = {1,2,3,4}
b = {1,2,3,5,6,7}

is_sub = a.issubset(b)
print(is_sub)

a.clear()
print(a)