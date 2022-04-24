# dan = 2
# num = 0

print("구구단을 외자~")

for dan in range(2, 10):
    print("======= [ " + str(dan) + "단! ]=======")
    for num in range(1, 10):
        print(str(dan) + " * " + str(num) + " = " + str(dan*num))
