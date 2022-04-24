for i in range(0, 10):
    message = ""
    if i % 3 == 0:
        message += "fizz"
        if i % 5 == 0:
            message += "buzz"
            print(message)
        else:
            print(message)
    else:
        if i % 5 == 0:
            message += "buzz"
            print(message)
        else:
            message = "*"
            print(message)