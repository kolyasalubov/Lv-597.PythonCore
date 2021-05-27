# У діапазоні від 1 до 10 визначають
# парні числа, які діляться на 2,
# непарні числа, які діляться на 3,
# числа, які не діляться на 2 і 3.

list_range = [x for x in range (10)]
list_range1 = [x for x in range (10) if x %2 == 0]
list_range2 = [x for x in range (10) if x %3 == 0]
list_range3 = [x for x in range (10) if x %2 != 0 and x %3 !=0]
print (list_range)
print (list_range1)
print (list_range2)
print (list_range3)