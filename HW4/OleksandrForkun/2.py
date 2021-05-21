# 2.Create a list that contains elements of integer type, then use the loop to change the type
# of these elements to a floating type. (Hint: use the built-in float () function).

list1 = [2, 4, 51, 22, 12]
list2 = []


def int_to_float(int_list, float_list):
    for element in int_list:
        element = float(element)
        float_list.append(element)


# test
int_to_float(list1, list2)
print(list1, list2, sep='\n')
