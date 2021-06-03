import re

def password(pas):
    check = 0
    while True:
        if len(pas) < 16:
            check += 1
            break
        if len(pas) >= 6:
            check += 1
            break
        elif re.search(["a-z"], pas):
            check += 1
            break
        elif re.search("[A-Z]", pas):
            check += 1
            break
        elif re.search("[0-9]", pas):
            check += 1
            break
        elif re.search("[_@$]", pas):
            check += 1
            break
        if check == 6:
            return f"Your pass is  correct, and ur pass is: {pas}"
        else:
            return "Your pass is not correct, your pass must contain from 6 to 16, [a-z], [0-9],[$#@]"

