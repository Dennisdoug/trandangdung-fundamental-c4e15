from random import randint
a = randint(1, 20)
b = randint(1, 20)

error = randint(-1, 1)
display_result = a + b + error
print(str(a) + ' + ' + str(b) + " =",display_result)

result = input("(Y / N)")

if display_result == a + b:
    if result == "y":
        print("Yay")
    if result == "n":
        print("Game over!")
else:
    if result == "y":
        print("Game over!")
    if result == "n":
        print("Yay")
