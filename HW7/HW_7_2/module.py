import re


def password(code):

    if not re.search("([a-z])", code):
        print("READ THE term and try again")
    elif not re.search("[A-Z]", code):
        print("READ THE term and try again")
    elif not  re.search("[0-9]", code):
        print("READ THE term and try again")
    elif not  re.search("[_@$]", code):
        print("READ THE term and try again")
    elif not len(code) >= 6 and not len(code) <= 16:
        print("READ THE term and try again")
    else:
        return f"Your password is correct, it is: {code}"