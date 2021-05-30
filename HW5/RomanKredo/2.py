#Task2 ask login while First
while True:
    login = input("Enter your login: ")
    if login == "First":
        print('Hello user', login)
        break
    print(f"User {login} doesn't exists")