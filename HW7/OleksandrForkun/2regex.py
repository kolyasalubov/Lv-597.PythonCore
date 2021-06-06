# Task1. Write a Python program to check the validity of password (input from users).

# Write a Python program to validate a password (entered by users).
#
# Verification:
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$ # @].
# The minimum length is 6 characters.
# The maximum length is 16 characters.

import re


def check_pass(password):
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*(\$|#|@)).{6,16}$')
    check = pattern.search(password)
    if check is not None:
        return True
    else:
        return False


# test


test_password1 = 'Ba$$721'
test_password2 = 'zaaaaaaaaaaaaaaaaaa'
print(check_pass(test_password1))
print(check_pass(test_password2))
