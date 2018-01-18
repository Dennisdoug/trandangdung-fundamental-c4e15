import random

attempts = 1
n = random.randint(1,100)
isCorrect = False
guess = int(input("Guess a number between 1-100: "))

while n != guess and attempts < 10:

    if guess < n:
        print("Higher...")
    elif guess > n:
        print("Lower...")
    guess = int(input("Take a guess: "))
    attempts += 1

if attempts == 10:
    print("\nSorry you reached the maximum number of tries")
    print("The correct number was ",n)

else:
    print("\nYou guessed it! The number was " ,n)
    print("You guessed it in ", attempts,"attempts")
