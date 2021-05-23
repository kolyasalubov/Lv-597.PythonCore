#Create a list that contains elements of integer type
# Use the loop to change the type of these elements to a floating type

list_of_int = [1, 2, 3, 4, 5] 

list_of_floats = []
for item in list_of_int:
    list_of_floats.append(float(item))

print(list_of_floats)
