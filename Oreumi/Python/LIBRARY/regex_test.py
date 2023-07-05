import re

pattern = r'apple'
string = "I have an apple and an orange."

result = re.search(pattern, string)
print(result)

pattern = r"b.t"
string = "bat, bet, bit, but, baat, beet"
result = re.findall(pattern, string)
print(result)

pattern = r"ab+c"
string = "ac, abc, abbc, abbbc, abdc"
result = re.findall(pattern, string)
print(result)

pattern = r"ab*c"
result = re.findall(pattern, string)
print(result)

pattern = r"[0-9]"
string = "0123456789"
result = re.findall(pattern, string)
print(result)

pattern = r"\d"
string = "I have 10 apples and 5 bananas"
result = re.findall(pattern, string)
print(result)

pattern = r"\w+"
string = "Hello, World! 123"
result = re.findall(pattern, string)
print(result)

pattern = r"^Hello"
string = "Hello, World! Hello, Python!"
result = re.findall(pattern, string)
print(result)

pattern = r"hon!$"
result = re.findall(pattern, string)
print(result)

pattern = r"a{2,3}"
string = "ab, abc, aabc, aaabc"
result = re.findall(pattern, string)
print(result)

pattern = r"a|b"
result = re.findall(pattern, string)
print(result)

pattern = r"(ab)+"
string = "ab, abab, ababc"
result = re.match(pattern, string)
print(result)
result = re.findall(pattern, string)
print(result)

string = "안녕하세요. 저의 전화번호는 !-010-1234-5678-!입니다. 다른 전화번호는 02-987-6543입니다. 1231!2131@1212 155542-10-1"
pattern = r"[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}"
result = re.findall(pattern, string)
print(result)

string="안녕하세요. 이메일 주소는 abc@example.com입니다. 다른 이메일은 ab_TE@hcu.co.kr이고, x_yz@hotmail.net도 있습니다."
pattern = r"\w+@\w+[.a-z]+[.a-z]*"
result = re.findall(pattern, string)
print(result)

string = "문장 속에는 다양한 URL이 있습니다. https://www.example.com/, http://subdomain.example.co.kr/, www.google.com, ftp://fileserver.example.org, 이렇게 다양한 형식의 URL이 있습니다."
pattern = r"[a-z0-9.:/-]+[0-9a-z./]+"
result = re.findall(pattern, string)
print(result)
result = re.sub(pattern, "", string)
print(result)