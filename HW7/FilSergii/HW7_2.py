'''
Write a Python program to check the validity of a password (input from users).

Validation :
At least 1 letter between [a-z]  [a-z]+
and 1 letter between [A-Z]. A-Z]+
At least 1 number between [0-9]. \d+
At least 1 character from [$#@]. $#@]+
Minimum length 6 characters. \S{6,16}
Maximum length 16 characters.

'''

import re

user_pass = input('Enter the password: ')

valid_count = re.search(r'\S{6,16}', user_pass)
valid_number = re.search(r'\d+', user_pass)
valid_letter = re.search(r'[a-z]+', user_pass)
valid_letter_up = re.search(r'[A-Z]+', user_pass)

if valid_count is None:
    print (f'Error! The password must have from 6 to 16 symbols!')
elif valid_number is None:
    print(f'Error! The password must have numbers 1 or more')
elif valid_letter is None:
    print (f'Error! The password must have letters 1 or more')
elif valid_letter_up is None:
    print (f'Error! The password must have upper letters 1 or more')
else:
    print('Your password is Good')
