while True:
    entered_login = input("enter login: ")
    print(f"hello my dear user {entered_login}" if entered_login == "First" else f"user {entered_login} doesn't exists" )
