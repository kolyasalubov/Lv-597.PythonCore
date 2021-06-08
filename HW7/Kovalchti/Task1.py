# A Python program to check the validity of password 

import re

def checking_pass(password):
    pattern = re.compile(r'(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[@$#]+)(?=.*[0-9]+).{6,16}')
    checking = pattern.fullmatch(password)
    if checking is not None:
        return True
    else:
        return False   


        
