sum = 0

for i in range(0, 101):
    if i % 3 == 0:
        sum += i

print("0 부터 100 사이의 모든 3의 배수의 합은 " + str(sum) + "입니다.")