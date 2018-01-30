numbers = [1, 6, 8, 1, 2, 1, 5, 6, 1, 4, 5, 2, 7, 8, 4, 5, 9, 2, 1, 6, 8, 0, 0, 5, 6]
x = int(input("Enter a number? "))
count = len([i for i in numbers if i == 1])
print(x, "appears " + str(count) + " times in the list")

#Without count() function
