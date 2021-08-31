import random
number = random.randint(1, 100)
#print(number)
#magic_number = int(input("What is the magic number? "))
guess = -1
while guess != number:
    guess = int(input("What is the guess? "))
    if guess < number:
        print("Higher")
    elif guess > number:
       print("Lower")
    else:
       print("You guessed it")
# guess > magic_number: