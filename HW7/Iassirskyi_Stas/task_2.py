import re


def validate_password(password):

    pattern_letters = re.compile('[a-z]', flags=re.IGNORECASE)
    pattern_numbers = re.compile('[0-9]')
    pattern_characters = re.compile('[$#@*&!]')


    if not len(password) >=6 and len(password) <=16:
        return 'Minimum 6 characters'

    elif not pattern_letters.findall(password):
        return 'Your password need to have a least one letter'

    elif not pattern_numbers.findall(password):
        return 'Your password need to have at least one number'

    elif not pattern_characters.findall(password):
        return 'Your password need to have some special character'

    else:
        return 'Access accept'



while True:

    check_password = input('Enter your password or "q" to exit\n')

    if check_password == 'q':
        print('Bye, bye')
        break

    else:
        print(validate_password(check_password))

