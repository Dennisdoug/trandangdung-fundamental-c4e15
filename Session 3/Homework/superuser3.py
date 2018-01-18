from getpass import getpass

attempts = 1

while attempts < 4:
    username = input ("username: ")
    password = input ("password: ")
    if username == "c4e":
        if password == "codethechange":
            print("Welcome, Superuser")
            break
        else:
            print("Wrong password")
    else:
        print("You are not superuser!")
    attempts += 1

if attempts == 4:
    print("You've been blocked from the server!")
