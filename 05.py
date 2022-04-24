number_ = input("정수를 입력하세요 : ")

number = int(number_)

for i in range(1, number + 1):
    if i < number:
        for j in range(1, i + 1):
            print(j, end="")
        print()
    elif i == number:
        for j in range(1, i + 1):
            print(j, end="")