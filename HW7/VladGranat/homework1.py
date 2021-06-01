def highest (a,b):

    '''
    Enter two numbers
    And take the highest one
    '''

    if a >= b:
        return a
    else:
        return b

a = input ("Enter 1 number: ")
b = input ("Enter 2 number: ")

print (highest(a,b))
print (highest.__doc__)