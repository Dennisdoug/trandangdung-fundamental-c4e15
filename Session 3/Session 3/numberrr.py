x = int(input("Enter a number: "))
digits = 0

while x > 0:
    digits += 1
    x //= 10
print(digits)
