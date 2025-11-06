while True:
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Too small")
        continue
    has_symbol = False
    for i in password:
        if not i.isalnum():
            has_symbol = True
            break
    if has_symbol == False:
        print("You have no characters. Please add a character.")
        continue
    print("Password accepeted!")
    break