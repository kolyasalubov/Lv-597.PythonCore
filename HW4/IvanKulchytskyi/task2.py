import random

list_size = random.randrange( 1, 10 )
list_of_numbers = list()

while list_size > 0:
    list_of_numbers.append( random.randrange( 1, 100 ) )
    list_size -= 1

print( f"original list: {list_of_numbers}; type of [0] element {type( list_of_numbers[0] )}" )
type( list_of_numbers[0] )

for item in range( len( list_of_numbers ) ):
    list_of_numbers[item] = float( list_of_numbers[item] )

print( f"transformed list: {list_of_numbers}" )