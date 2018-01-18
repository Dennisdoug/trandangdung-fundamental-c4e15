from random import randint

x = randint(1, 100)
loop = True

while loop:
    num = int(input("Enter a number 1 - 100: "))

    if num == x:
        print("Bingo")
        loop = False
    elif num < x:
        print("A little too small")
    else:
        print("A little too large")
