# x = int(input("x = "))
# operation = input("Operation (+,-,*,/): ")
# y = int(input("y = "))
#
# result = 0
# if operation == '+':
#     result = x + y
# elif operation == '-':
#     result = x - y
# elif operation == '*':
#     result = x * y
# elif operation == '/':
#     result = x / y
# else:
#     print("Invalid operation")
#
# print("{0} {1} {2} = {3}".format(x, operation, y, result))


def eval(x, y, op):

    result = 0

    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y

    return result

x = int(input("x = "))
y = int(input("y = "))
op = input("op = ")
result = eval(x, y, op)
print("{0} {1} {2} = {3}".format(x, op, y, result))
