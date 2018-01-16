from getpass import getpass
username = input ("username: ")
password = input ("password: ")
if username == "c4e":
    if password == "codethechange":
        print("Welcome, Superuser")
    else:
        print("Wrong password")
else:
    print("Fuck off hacker!")
