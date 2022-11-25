import random

print("Welcome to an Auto-mated Rock, Paper, Scissors Game!")
print("Keep playing until you feel like quitting. We'll keep count to see who wins.")
user_wins = 0
computer_wins = 0
cat = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == "rock" and computer_pick == "rock":
        print("Cat")
        cat += 1
    elif user_input == "paper" and computer_pick == "paper":
        print("Cat")
        cat += 1
    elif user_input == "scissors" and computer_pick == "scissors":
        print("Cat")
        cat += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("And the Cat got", cat, ".")

if user_wins > computer_wins:
    print("You won!")
if computer_wins > user_wins:
    print("You lost! The computer beat you.")
