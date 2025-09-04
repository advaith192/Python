print("Choose your ride:")
print("1. Bike")
print("2. Car")
choice=int(input("Pick your choice: "))
if choice == 1:
    print("You have selected Bike. What type would you like?")
    print("1. Scooty")
    print("2. Scooter")
    choice2=int(input("Pick your type: "))
    if choice2 == 1:
        print("You have selected Scooty. Your ride will be on its way.")
    elif choice2 == 2:
        print("You have selected Scooter. Your ride will be on its way.")
    else:
        print("Wrong input. Try again.")
elif choice == 2:
    print("You have selected Car. What type would you like?")
    print("1. Sedan")
    print("2. SUV")
    choice3=int(input("Pick your type: "))
    if choice3 == 1:
        print("You have selected Sedan. Your ride will be on its way.")
    elif choice3 == 2:
        print("You have selected SUV. Your ride will be on its way.")
    else:
        print("Wrong input. Try again.")
else:
    print("Wrong input. Try again")