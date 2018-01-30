a = int(input("How many B bacterias are there? "))
b = int(input("How much time in minutes will we wait? "))

if b % 2 == 0:
    total = a * b
    total = print("After " + str(b) + " minutes, we would have " + str(total) + " bacterias.")
else:
    total = a * (b - 1)
    total = print("After " + str(b) + " minutes, we would have " + str(total) + " bacterias.")
