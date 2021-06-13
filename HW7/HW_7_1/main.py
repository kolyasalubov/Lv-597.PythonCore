import module
print("What type of figure do u want to take a square: ")
print("1 - Triangle ")
print("2 - Rectangle ")
print("3 - Circle ")

num1 = int(input("Enter from 1 to 3: "))
while num1 > 3 or num1 <= 0 and num1 == int:
    print("PLS again  ")
    num1 = int(input("Enter from 1 to 3: "))


if num1 == 1:
    item = module.triangle_square(int(input("Input height: ")), (int(input("Input sum of sides of triangle: "))))
elif num1 == 2:
    item1 = module.rectangle_square(int(input("Input first side: ")), (int(input("Input second side: "))))
else:
    item2 = module.circle_square(int(input("Input radius: ")))