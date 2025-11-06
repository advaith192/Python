import random
while True:
    user_action = input("Enter an action: rock, paper or scissors: ")
    possible_actions = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    if user_action == computer_action:
        print("You tied with", user_action, "and", computer_action)
    elif user_action == "rock" and computer_action == "paper":
        print("You lost with", user_action, "and", computer_action)
    elif computer_action == "rock" and user_action == "paper":
        print("You won with", user_action, "and", computer_action)
    elif user_action == "paper" and computer_action == "scissors":
        print("You lost with", user_action, "and", computer_action)
    elif computer_action == "paper" and user_action == "scissors":
        print("You won with", user_action, "and", computer_action)
    elif user_action == "scissors" and computer_action == "rock":
        print("You lost with", user_action, "and", computer_action)
    elif computer_action == "scissors" and user_action == "rock":
        print("You won with", user_action, "and", computer_action)
    else:
        print("Wrong input")
     
    answer = input("Would you like to play again? ")
    if answer == "No" or answer == "no":
        break