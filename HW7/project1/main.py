import module as m

print("Check is your password ready to use: ")
print(""" At least 1 letter between [a-z] and 1 letter between [A-Z].
          At least 1 number between [0-9].
          At least 1 character from [$#@].
          Minimum length 6 characters.
          Maximum length 16 characters. """)



while True:
    lol = m.password1(input("Input pass: "))


#Help
#IF pass is correct, I don't know how to return line 17 in module.py