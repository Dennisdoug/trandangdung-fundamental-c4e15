print('''
Hi there,
Think about a number from 1 - 100, then press Enter
''')

lo = 0
hi = 100

loop = True
while loop:
    mid = (lo + hi) // 2
    answer = input("Is {0} your number: ".format(mid))
    if answer.lower() == "c":
        print("I knew it")
        loop = False
    elif answer.lower() == "s":
        hi = mid
    elif answer.lower() == "l":
        lo = mid
