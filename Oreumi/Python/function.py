def greet(name):
    print("반갑습니다! {} 여려분.".format(name))

def add(a,b = 2):
    return a+b

def sum(*args):
    total = 0
    for i in args:
        total += i
    return total

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def outer_function():
    x = 10
    def inner_function():
        print(x) # 외부 함수의 변수 사용
        inner_function()
outer_function() # 출력: 10

global_var = 100 # 전역 변수
def my_function():
    local_var = 50 # 지역 변수
    print("전역 변수:" , global_var)
    print("지역 변수:" , local_var) 
my_function()
print("전역 변수:" , global_var) 

def get_person():
    return "John", 25, "john@example.com"
name, age, email = get_person()

def add(a: int, b: int) -> int:
    return a + b

# 파이썬의 함수는 일급함수
def greet(name):
    return f"Hello, {name}!"
hello = greet # 함수를 변수에 할당
print(hello("Gppi")) # 변수로 함수 호출 

def apply_operation(func, x, y):
    return func(x, y)
def add(a, b):
    return a + b
result = apply_operation(add, 2, 3) # 함수를 인자로 전달하여 실행
print(result)

# Lambda 함수
add = lambda a, b: a + b 
result = add(2, 3) # Lambda 함수 호출
print(result)

numbers = [1,2,3,4,5]
squared = list(map(lambda x:x+1, numbers))
data = list(map(int, input().split()))
print(squared)

numbers = ["letter", "bigger"]
uppers = list(map(lambda x:x.upper(), numbers))
print(uppers)
