try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError
    else:
        print("Age is valid")
except ValueError:
    print("Age is not valid")