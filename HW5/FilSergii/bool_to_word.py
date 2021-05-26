def bool_to_word(boolean):
    if boolean is True:
        return 'Yes'
    else:
        return 'No'

boolean = bool(input("Enter a boolean what need to conver: "))
print (bool_to_word(boolean))
