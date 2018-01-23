from random import choice, randint

for k in range(10):
    wordlist = ["pizza", "hamburger", "mac and cheese", "corn dog", "burrito", "nuggets", "steak", "potato chips", "sandwich", "spaghetti"]
    word = choice(wordlist)
    n = list(word)
    for i in range(len(n)):
        j = randint(0,len(n)-1)
        a = n[i]
        n[i] = n[j]
        n[j] = a

    print(*n, sep = ' ')


    guess = input("Your answer: ")
    if guess != word:
        print("Wrong!")
    else:
        print("Hura")
