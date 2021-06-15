# Task1. A Python program to check the validity of password (input from users).

import re

def check_pass(password):
    pattern = re.compile(r'(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[@$#]+)(?=.*[0-9]+).{6,16}')
    check = pattern.search(password) 
    return True if check else False

