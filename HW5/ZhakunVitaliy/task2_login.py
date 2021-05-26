while True:
    if (login := input("Enter the login here: ")) == "First":
        print("Welcome to Your account!".center(40,"="))
        break
    elif login.isalpha() != True:
        print("INCORRECT INPUT".center(40,"="))
        print("Must contain only alphabetic symbols".center(40,"."))
        print("-"*40)
        continue
    else:
        print("INCORRECT LOGIN".center(40,"="))
        print("Try once more".center(40,"."))
        print("-"*40)
        continue
