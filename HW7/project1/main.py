import module as m

print("Check is your password ready to use: ")
print(""" At least 1 letter between [a-z] and 1 letter between [A-Z].
          At least 1 number between [0-9].
          At least 1 character from [$#@].
          Minimum length 6 characters.
          Maximum length 16 characters. """)

lol = m.password(input("Input pass: "))

