number = input("정수를 입력하시오 : ")
divisor = ""

number = int(number)

for i in range(1, number + 1, 1):
    if number % i == 0:
        divisor += str(i)
        divisor += " "

print("약수 : " + divisor)