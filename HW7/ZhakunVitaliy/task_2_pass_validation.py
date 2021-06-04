import re

while True:
    password = input("Please, enter the valid password: ")
    if not re.search(r"^.{5,17}$", password):
        print("The password must be at least 6 and 18 as maximum characters long")
    elif not re.search(r"(?=.*[a-z])", password):
        print("The password must contain at least 1 lowercase alphabetic characters")
    elif not re.search(r"(?=.*[A-Z])", password):
        print("The password must contain at least 1 uppercase alphabetic characters")
    elif not re.search(r"(?=.*[0-9])", password):
        print("The password must contain at least 1 digital characters")
    elif not re.search(r"[@|#|$]", password):
        print("The password must contain at least 1 special characters ('@','#' or '$')")
    else:
        print("Your password was successfully created!".center(50, "="))
        break
