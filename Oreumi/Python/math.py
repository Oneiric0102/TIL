a, b = input("").split(" ")

a = int(a)
first_a = a
b = int(b)
first_b = b
while b!=0:
    a,b = b, a%b

print(f"최대공약수: {a}")
print(f"최소공배수: {first_a*first_b/a}")

n = input("소인수 분해 : ")
factors = []

while n%2 == 0:
    factors.append(2)
    n//=2

i = 3
while i*i <=n:
    while n%i ==0:
        factors.append(i)
        n//=i
    i+=2

if n>1:
    factors.append(n)

print(factors)