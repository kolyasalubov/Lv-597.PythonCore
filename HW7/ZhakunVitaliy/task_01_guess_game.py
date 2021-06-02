
from random import randint

randnum = randint(1, 100)
while True:
    guess = int(input("Enter Your guess: "))
    if guess == randnum:
        break
    elif guess < randnum:
        print("Too Low!")
    else:
        print("Too High!")
print("You guessed correctly with: ", guess)
