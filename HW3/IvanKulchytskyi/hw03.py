import random

# get random numbers
first_number = random.randrange( 100 )
second_number = random.randrange( 100 )
print( "before swap: first= ", first_number, " second= ", second_number )

# swap numbers
second_number += first_number
first_number = second_number - first_number
second_number -=first_number
print( " after swap: first= ", first_number, " second= ", second_number )