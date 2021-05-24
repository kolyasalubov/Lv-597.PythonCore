import math

num = int(input("Enter some number greater than 0: "))

if num > 0:
    print("The factorial of your number is ", math.factorial(num))
else:
    print("Try again!")