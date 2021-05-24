

num = int(input("Enter some number: "))
num_1 = 0
num_2 = 1

print(num_1)
print(num_2)

for num in range(2, num):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3)
else:
    print("The end!")