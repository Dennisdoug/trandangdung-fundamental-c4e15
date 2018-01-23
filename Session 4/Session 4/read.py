favs = ["teaching", "netflix", "death note"]
print(*favs, sep=", ")

# for fav in favs:
#     print(fav, end=", ")
# print()
print("*" * 10)

# position = 1

# for fav in favs:
#     print("{0}. {1}".format(position, fav))
#     position += 1

for index, fav in enumerate(favs):
    s = "{0}. {1}".format(index + 1, fav)
    print(s)
    # print(index, fav)

# for (i, v) in enumerate(["teaching", "netflix", "death note", "porn"]):
#     print(i, v)
