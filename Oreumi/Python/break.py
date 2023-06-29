a = int(input("숫자를 입력하세요 : "))

for i in range(1,101):
    print(i)
    if i == a:
        print("종료!")
        break

while True:
    a = input("내가 좋아하는 과일 맞추기!")
    if a=="배":
        print("맞았습니다!")
        break
    else:
        print("틀렸습니다!")