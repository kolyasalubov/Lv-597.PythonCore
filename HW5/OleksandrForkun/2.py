# 2.Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is different, send an error message.
# (need to use loop while)


login = input('Enter your login please: ')
while login != 'First':
    print('Login is invalid. Try again')
    login = input('Enter your login please: ')
else:
    print(f'Welcome {login}!')
