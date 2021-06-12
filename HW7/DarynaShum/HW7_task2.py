import re


password = input("""Create the password which has two letters between(a-z),
two letters between(A-Z), two numbers between(0-9) and some character ($#@)
minimum length 6 characters.
For example: boOK12@ or boOK12
Your password:""")


pat =  re.search("^[a-z]{1,2}([a-z]?[A-Z]?[A-Z]?[A-Z]?)(\d\d)([@#$]?)", password)
 
if pat:
    print("The password is valid!")
else:
    print("The password is invalid!")

if len(password) < 6:
    print("The password is short!")

