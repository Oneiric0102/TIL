str1 = "hello"
str2 = "world!"

print(str1 + " " + str2)

str1 = "문자열 곱하기 연산" * 10
print (str1)

str1 = "문자열 a 인덱싱 1"
#["문", "자", "열", " ", "a"]
print(str1[4])

str1 = "문자열 apple 인덱싱 2"
print(str1[4:9])
print(str1[9:])
print(str1[:4])

str1 = "글자수 세기"
print(len(str1))

text = "hello world!"
a = []
for i in text:
    a.append(i)
print(a)

print(".".join(a))

a = ["안녕", "오늘도", "수고했어", "!"]
print("\n".join(a))