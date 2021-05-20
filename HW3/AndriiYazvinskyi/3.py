a = int(input("Input u first number: "))
b = int(input("Input u second number: "))

print("Your str is: ", a, b)

a, b = b, a
print("Your replacement str  is: ", a, b)

a = a + b
b = a - b
a = a - b
print("Your replacement str  is: ", a, b)
