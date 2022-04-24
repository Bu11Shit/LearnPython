underBar = "---"
lengthBar = "|    "

gameSize = int(input("게임판 크기 : "))
#print(" ", underBar, end="")

for i in range(1, gameSize + 1):
    print()
    for j in range(1, gameSize + 1):
        print(" ", underBar, end="")

    print("\n", lengthBar * int(gameSize + 1), "  ", end="")
print()
for j in range(1, gameSize + 1):
    print(" ", underBar, end="")
    