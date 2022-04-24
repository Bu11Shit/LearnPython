n = 0
total = 0

n = input("n의 값을 입력하시오 : ")

n_ = int(n)
for i in range(1, n_ + 1):
    total += pow(i, 2)

print("계산값은 " + str(total) + "입니다.")