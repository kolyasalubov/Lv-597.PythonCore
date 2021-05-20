print ("Let`s take four numbers, first number: ")
first = input()
print ("Second number: ")
second = input()
print ("Third number: ")
third = input()
print ("And the last one: ")
last = input()
print (first,second,third,last)
str = (first,second,third,last)

result = int(first) * int(second) * int(third) *int(last)
print ("result of all numbers:", result)

print (str [:: -1])

l = [str]
l.sort()
print(l)
