maxNum = 20
n = 2



for i in range(n, maxNum + 1):
    isPrime = True
    for j in range(n, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)
