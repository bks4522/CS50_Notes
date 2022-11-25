print("Welcome to Chase's Movie Quiz!")

playing = input("Do you want to play? Yes or No: ")

if playing.lower() == "yes":
    print("Ok, let's play.")
else:
    print("Ok, goodbye.")
    quit()

score = 0

answer1 = input(
    "What was the name of the actress who played Dorothy in 'The Wizard of Oz'? "
)
if answer1.lower() == "judy garland":
    print("Correct")
    score += 1
else:
    print("Wrong!")

answer2 = input("What was the first movie to have an original soundtrack? ")
if answer2.lower() == "king kong":
    print("Correct")
    score += 1
else:
    print("Wrong!")

answer3 = input("What item was the Dude trying to get back in 'The Big Lebowski'? ")
if answer3.lower() == "rug":
    print("Correct")
    score += 1
else:
    print("Wrong!")

answer4 = input(
    "Who was the voice actor who played both Scooby-Doo and Fred in the original 'Scooby-Doo'? "
)
if answer4.lower() == "frank welker":
    print("Correct")
    score += 1
else:
    print("Wrong!")

answer5 = input("What is the highest grossing animated Disney movie? ")
if answer5.lower() == "frozen ii":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

print("Your score is " + str(score) + ".")
if score == 5:
    print("Damn, son, you smart!")
elif score == 4:
    print("Pretty good! Almost a perfect score!")
elif score == 3:
    print("Not too shabby!")
elif score == 2:
    print("Keep studying!")
else:
    print("You suck!")
