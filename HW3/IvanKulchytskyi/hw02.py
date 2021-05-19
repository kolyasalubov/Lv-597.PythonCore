# 0) get number
while True:
    entered_number_as_string = input( "Give me 4 digit number: " )
    if entered_number_as_string.isnumeric() :
        entered_number = int( entered_number_as_string )
        if entered_number > 999 and entered_number < 10000 :
            break

# 1)
digits_multiplication = (
    int( entered_number_as_string[0] ) *
    int( entered_number_as_string[1] ) *
    int( entered_number_as_string[2] ) *
    int( entered_number_as_string[3] )
)

# 2)
#  2.1) with list
entered_number_list = list( entered_number_as_string )
entered_number_list.reverse()
reverse_number1 = ''.join( entered_number_list )
#  2.2) string slice
reverse_number2 = ''.join( entered_number_as_string[::-1] )
#  2.3) with arifmetic 
reverse_number3 = 0
temp_number = entered_number
while temp_number > 0:
    temp_modulus = temp_number % 10
    reverse_number3 = reverse_number3 * 10 + temp_modulus
    temp_number = temp_number // 10


# 3)
entered_number_list.sort()
sorted_number_string = ''.join( entered_number_list )

print( "\nNumber:", entered_number_as_string, 
       "\n1) Multiplication:", digits_multiplication,
       "\n2.1) Reverse:", reverse_number1,
       "\n2.2) Reverse:", reverse_number2,
       "\n2.3) Reverse:", reverse_number3,
       "\n3) Sorted:", sorted_number_string
)
