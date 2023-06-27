fruits = ["사과", "수박", "배"]
prices = [2500, 15000, 5000]
amounts = [5, 6, 3]
for fruit in fruits:
    print(fruit)

# range
for i in range(0,5):
    print(i)

for idx, x in enumerate(fruits):
    print(idx, x)

for fruit, price, amount in zip(fruits,prices,amounts):
    profit = price * amount
    print(fruit, price, amount, profit)

for i in range(0, 10):
    if i == 0:
        break
    print(i)

for fruit in reversed(fruits):
    print(fruit)

with open("D:\\project\\TIL\\Oreumi\\Python\\test.txt", "r", encoding='utf-8') as f:
    text = f.read().split('\n')
    for idx, name in enumerate(text):
        print(f'{idx+1}번째 학생: {name}')

a = "Hello World!"
length = 0
for i in a:
    length+=1
print(length)

a = ["1", "2", "3", "4", "5"]
sum = 0
for i in a:
    sum+=int(i)
print(sum)

a = int(input("팩토리얼 입력 : "))
factorial = 1
for n in range(1,a+1):
    factorial*=n
print(factorial)