import re


def password1(pas):

    if not re.search("([a-z])", pas):
        print("READ THE term and try again")
    elif not re.search("[A-Z]", pas):
        print("READ THE term and try again")
    elif not  re.search("[0-9]", pas):
        print("READ THE term and try again")
    elif not  re.search("[_@$]", pas):
        print("READ THE term and try again")
    elif not len(pas) >= 6 and not len(pas) <= 16:
        print("READ THE term and try again")
    else:
        return f"Your pass is  correct, and ur pass is: {pas}"

