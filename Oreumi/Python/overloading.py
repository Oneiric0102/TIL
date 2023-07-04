class Calculator:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c
calculator = Calculator()
print(calculator.add(2, 3)) # 오류 발생!
print(calculator.add(2, 3, 4)) # 9