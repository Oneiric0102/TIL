import time
import functools

def calculation(func):
    def wrapper(*args, **kwargs):
        print("데코레이터 1 시작")
        func(*args, **kwargs)
        print("데코레이터 1 종료")
    return wrapper

def calculation2(func):
    def wrapper(*args, **kwargs):
        print("데코레이터 2 시작")
        func(*args, **kwargs)
        print("데코레이터 2 종료")
    return wrapper

@calculation
@calculation2
def add(a,b):
    print(a+b)

add(3,5)

#-----------------------------------------------------
def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elasped = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r'%(k,w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r'%(elasped, name, arg_str, result))
        return result
    return clocked

@functools.cache
@clock
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))