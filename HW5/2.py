login = str(input(f'Put your login here:\n'))

while login != 'First':
    print(f'Error!!!!!!\nYour login "', login, '" does not have rights!\n**P.S. Check if CAPS LOCK is not working..**')
    break
else:
    print(f'Greetings!!!\nWelcome, "', login, '"!!!')