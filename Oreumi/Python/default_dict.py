from collections import defaultdict

my_dict = defaultdict(int)

my_dict['사과'] += 1
my_dict['바나나'] += 1
my_dict['수박'] += 1

print(my_dict)