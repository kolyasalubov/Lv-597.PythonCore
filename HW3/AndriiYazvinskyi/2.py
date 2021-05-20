num1 = int(input("Input your four-digit number: "))

if num1 > 9999:
    print("Your number must be lower than 9999")
elif num1 < 1000:
    print("Your number must be upper than 999")
else:
    a = num1 // 1000
    b = num1 // 100 % 10
    c = num1 // 10 % 10
    d = num1 % 10
    print("The multiplication is: ", a * b * c * d)

    print("--------------------------------------------------------------")

    num1 = str(num1)
    print("Your reverse number: ", num1[::-1])

    print("--------------------------------------------------------------")

    list1 = [i for i in num1]
    list1.sort()
    separator = ', '
    print("Your sort number: ", separator.join(list1))
