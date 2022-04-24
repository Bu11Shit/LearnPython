myList = [ 11, 22, 23, 99, 81, 93, 35 ]

sum = 0

myList.sort()

for i in range (0, len(myList)):
    sum += myList[i]

print(sum)