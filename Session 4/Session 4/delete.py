favs = ["teaching", "netflix", "death note"]
print(*favs, sep=", ")
print("*" * 10)
for index, fav in enumerate(favs):
    s = "{0}. {1}".format(index + 1, fav)
    print(s)

x = int(input("Enter a number you want to delete: "))
favs.pop(x - 1)

print(favs)
