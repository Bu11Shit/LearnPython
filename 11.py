a = input("첫 번째 정수를 입력하시오 : ")
b = input("두 번째 정수를 입력하시오 : ")

biggest_common_divisor = 0

a_ = int(a)
b_ = int(b)

isBigger = True
if a_ > b_:
    isBigger = True
elif b_ > a_:
    isBigger = False

if isBigger == True:
    for i in range(1, b_):
        for j in range(1, a_):
            if b_ % j == 0 and a_ % j == 0:
                biggest_common_divisor = j
else:
    for i in range(1, a_):
        for j in range(1, b_):
            if a_ % j == 0 and b_ % j == 0:
                biggest_common_divisor = j

print(a + "과(와) " + b + "의 최대 공약수는 " + str(biggest_common_divisor) + "입니다.")