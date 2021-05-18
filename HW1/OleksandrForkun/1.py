# 1.Output question “What is your name?“,
#                                    “How old are you?“,
#                                    “Where do you live?“.
# Read the answer of user and output next information: “Hello, (answer(name))“,
# “Your age is  (answer(age))“,
# “You live in  (answer(city))“.

name = input('What is your name? ')
age = int(input('How old are you? '))
location = input('Where do you live? ')

print('Hello, {}! Your age is {} y.o. You live in {}.'.format(name, age, location))
