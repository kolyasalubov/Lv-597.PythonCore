'''
#First var

user_login = str
while user_login != 'First':
    user_login = input('Enter your login: ')
    if user_login == 'First':
        print(f'Hello {user_login}!')
    else:
        print(f'Wrong login. Try again\n')

#Second var:

while True:
    user_login = input('Enter your login: ')
    if user_login != 'First':
        print('Error! Wrong login. Try again')
    else:
        break
print(f'Hello {user_login}! Nice to meet you :)')
'''

while True:
    user_login = input('Enter your login: ')
    if user_login == 'First':
        print(f'Hello {user_login}!')
        break
    else:
        print(f'Wrong login. Try again\n')
