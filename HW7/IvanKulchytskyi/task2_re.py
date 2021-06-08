import task2_module as t2mod

def check_password(password):
    message = "BAD PASSWORD: The password"
    less_than = "contains less than 1"
    if t2mod.re_is_to_short(password):
        print(f"{message} is to short")
        return False
    elif t2mod.re_is_to_long(password):
        print(f"{message} is too long")
        return False
    elif not t2mod.re_has_lower(password):
        print(f"{message} {less_than} lowercase letter")
        return False
    elif not t2mod.re_has_upper(password):
        print(f"{message} {less_than} uppercase letter")
        return False
    elif not t2mod.re_has_digit(password):
        print(f"{message} {less_than} digit")
        return False
    elif not t2mod.re_has_special_characters(password):
        print(f"{message} {less_than} special character")
        return False
    else:
        return True

## setting minimal and maximal length
t2mod.minimal_length = 6
t2mod.maximum_length = 16

while True:
    if check_password(input("\nEnter password:")):
        print("Strong password!!!")
        break
