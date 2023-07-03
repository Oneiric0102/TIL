class Car:
    window = 2

    def __init__(self, people):
        self.people = people
        self.window = 2
        self.wheel = 4

    def brake(self):
        print(f"{self.people}(이)가 brake!")

    def accelerate(self):
        print("accelerate!")

my_car = Car("이민주")
my_car.brake()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
rectangle = Rectangle(width=4, height=5)
print(f"너비: {rectangle.width} 높이: {rectangle.height}")
print(rectangle.area())

class Animal:
    def play_sound(self):
        pass

class Cat(Animal):
    def __init__(self, sound, name, legs=4):
        self.legs = legs
        self.sound = sound
        self.name = name
    def play_sound(self):
        return f"{self.name}: {self.sound * 2}"
    
class Dog(Animal):
    legs = 4
    def __init__(self, sound, name, legs=4):
        self.legs = legs
        self.sound = sound
        self.name = name
    def play_sound(self):
        return f"{self.name}: {self.sound * 3}"
    
animals = [Cat(name = "르미", sound = "Meow"), Dog(name = "스트", sound = "Bark")]
print(animals[0].play_sound())
print(animals[1].play_sound())

class BackAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
account = BackAccount("12345678", 1000000)
# error
# print(account.__balance)
print(account.get_balance())