my_list = list(range(20,0,-4))

print('BEFORE'.center(40, "="))
print(f"my_list = {my_list}")

for i in range(len(my_list)):
    my_list[i] = float(my_list[i])
    
print('AFTER'.center(40, "="))    
print(f"my_list = {my_list}")