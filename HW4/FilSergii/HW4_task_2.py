'''
Create a list that contains elements of integer type,
then use the loop to change the type of these elements to a floating type. 
(Hint: use the built-in float () function). 
'''
list_count = int(input('How many elements are in list?\n'))

list_numbers = [int(input('Enter a integer number: ')) for item in range(list_count)]

for item in range(len(list_numbers)): #or we can use "list_count" instead "len(list_number)"
    list_numbers[item] = float(list_numbers[item])

#list_numbers = [float(item) for item in list_numbers]

print(f'Float list: {list_numbers}')
    

            
