favs = ["teaching", "netflix", "death note"]

print("Hi there, here are your favorite things so far:")
print(*favs, sep=", ") #pythonic

new_fav = input("Name one thing you want to add: ")
favs.append(new_fav)

print(*favs, sep=", ") #seperator
