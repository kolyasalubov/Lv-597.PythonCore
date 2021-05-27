#A script that checks the login that the user enters using while loop

while True:
    attempt_login = input("please enter your login: ")
    print(f"Welcome back {attempt_login}" if attempt_login == "First" else f"{attempt_login} access denied")