
def login():
    enter_login = input('Enter your login: ')
    if enter_login == 'First':
        print('Hello!')
    else:
        print('Login is incorect')
        login()

login()
