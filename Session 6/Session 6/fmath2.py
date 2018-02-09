from random import randint, choice
from calc import eval
x = randint(1, 20)
y = randint(1, 20)

operation = choice(["+", "-", "*", "/"])


error = randint(-1, 1)
display_result = eval(x, y, operation) + error
# if operation == '+':
#     result = x + y + error
# elif operation == '-':
#     result = x - y + error
# elif operation == '*':
#     result = x * y + error
# elif operation == '/':
#     result = x / y + error
print(str(x) +  operation  + str(y) + " =",display_result)

solution = input("(Y / N)")


if error == 0:
    if solution == "y":
        print("Yay")
    if solution == "n":
        print("Game over!")
else:
    if solution == "y":
        print("Game over!")
    if solution == "n":
        print("Yay")
