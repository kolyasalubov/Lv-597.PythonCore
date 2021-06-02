import re

def check_password(password):
    pattern = re.compile(r'(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[@$#]+)(?=.*[0-9]+).{6,16}')
    check = pattern.fullmatch(password)
    return True if check else False

print(check_password('aaAA11'))