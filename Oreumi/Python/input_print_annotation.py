age = input("나이를 입력해주세요: ")
name = input("이름을 입력해주세요: ")

print(f"저는 개발자 {name}, 나이 {age}세 입니다. 잘부탁드립니다!")

a = int(input("첫번째 숫자를 입력하세요: "))
b = input("두번째 숫자를 입력하세요: ")

print("합산 : {}".format(a+int(b)))

#한줄 주석처리

"""여러줄 주석처리
1
2
3
"""

def add(num1, num2, num3):
    """
    add 함수입니다.
        Args:
            a `str` : a value
            b `int` : b value
            c `str` : c value
        Returns:
            None
    """
    return num1 + num2 + num3