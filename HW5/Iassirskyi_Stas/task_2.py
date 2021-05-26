check_login = 'First'

while True:
    login = input('Enter your login \nor enter "q" to exit\n ')
    if login == 'q':
        break
    elif login == check_login:
        print(f'Welcome back {login}')
        continue
    elif login != check_login:
        print('The login is invalid')
        continue

