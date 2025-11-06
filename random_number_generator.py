import random
playing = True
randnum = random.randint(1,9)
while playing == True:
    guess = int(input("Enter a number 1-9: "))
    if guess == randnum:
        print("You win!")
        break
    else:
        print("Try again")