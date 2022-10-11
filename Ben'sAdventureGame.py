loop = 1
print("Welcome to Ben's Adventure Game!")
print("--------------------------------")
print("--------------------------------")
print("--------------------------------")
while True:
    while loop == 1:
        if loop == 1:
            # intro
            print("You wake up in a creepy castle. Spooky.")
            print("You see a fairy hovering above you. It speaks to you!")
            print(
                '"Hello, human. I have been sent to aid you on your quest. You have to slay an evil wizard and save a beautiful princess. Too easy, right? Go through that door in front of you to begin."'
            )
            choice1 = input("Go or stay? ")
        if choice1.strip().lower() == ("go"):
            loop = 2
        elif choice1.strip().lower() == ("stay"):
            print("\"C'mon, man! Let's go!\"")
            print("_________________________")
        else:
            print("Try again, this is a simple text game.")

        # Room1
    while loop == 2:
        if loop == 2:
            print("______________________________")
            print("You go through the first door.")
            print("It smells bad in here. You see bones on the floor.")
            print('"Ok, human, go through the door with the skull and cross-bones."')
        choice2 = input("Go or stay? ")
        if choice2.strip().lower() == ("go"):
            loop = 3
        elif choice2.strip().lower() == ("stay"):
            print("\"C'mon, man! The princess won't rescue herself!\"")
            print("_________________________________________________")
        else:
            print("Try again, this is a simple text game.")

    # Room2
    while loop == 3:
        if loop == 3:
            print("_____________________________________")
            print("You open the door and enter the room.")
            print(
                "You see a giant spider hurling itself at you! This thing is massive!"
            )
            print('"Quick, human, smack it!"')
            choice3 = input("Smack it or panic? ")
        if choice3.lower().strip() == ("smack it"):
            print("_____________________________")
            print("The spider crumples and dies.")
            print("That wasn't so tough, was it?")
            print('"Ok, let\'s keep going. Open the door in front of you."')
            loop = 9
            while loop == 9:
                choice4 = input("Go or stay? ")
                if choice4.strip().lower() == ("go"):
                    loop = 4
                elif choice4.strip().lower() == ("stay"):
                    print(
                        '"You literally just killed a man-eating spider. Quit being a coward!"'
                    )
                    print(
                        "______________________________________________________________________"
                    )
                else:
                    print("Try again, this is a simple text game.")
        elif choice3.lower().strip() == ("panic"):
            print("The spider eats you. Bummer, man.")
            panic_inp = input("Do you want to start over? Y/N ")
            if panic_inp.lower() == ("n"):
                exit()
            elif panic_inp.lower() == ("y"):
                loop = 1
            else:
                print("Try again, this is a simple text game.")
        else:
            print("Try again, this is a simple text game.")

    # Room3
    while loop == 4:
        if loop == 4:
            print("_______________________________________________________")
            print("You enter into what appears to be an apothecary's shop.")
            print("A glassy-eyed hipster greets you.")
            print('"Sup, man! Heard about the quest. Far out. Want some help?"')
            choice5 = input("Yes or no? ")
        if choice5.strip().lower() == ("no"):
            print(
                "The fairy admonishes you: \"Don't be an idiot! You need help if you're going to slay an evil wizard!\""
            )
            print(
                "__________________________________________________________________________________________________"
            )
        elif choice5.strip().lower() == ("yes"):
            print("________________________________")
            print("The hipster gives you an elixir.")
            print(
                "\"This stuff is fire, man. Don't take it until it's time, or you'll die, bruh. Serious vibe-killer. Need anything else?\""
            )
            loop = 10
            while loop == 10:
                choice6 = input("Yes or no? ")
                if choice6.strip().lower() == ("yes"):
                    print(
                        'The fairy admonishes you again: "Quit wasting time! You don\'t need anything else!"'
                    )
                    print(
                        "________________________________________________________________________________"
                    )
                elif choice6.strip().lower() == ("no"):
                    loop = 5
                else:
                    print("Try again, this is a simple text game.")
        else:
            print("Try again, this is a simple text game.")

    # Room4
    while loop == 5:
        if loop == 5:
            print(
                "_______________________________________________________________________"
            )
            print(
                "You leave the hipster apothecary's shop and descend a winding staircase."
            )
            print("While going down the staircase, you see a skeleton.")
            print('The fairy points at it: "Check it out!"')
            print(
                "You investigate the skeleton and find a key lodged inside the skull. Ouch."
            )
            choice7 = input("Take it or leave it? ")
        if choice7.lower().strip() == ("take it"):
            print("________________________________________________________")
            print("You grab the key and continue down the winding staircase.")
            print("The light becomes fainter and fainter. You hesitate.")
            print('"C\'mon, human! You need to keep going!"')
            loop = 11
            while loop == 11:
                choice8 = input("Go or stay? ")
                if choice8.strip().lower() == ("go"):
                    loop = 6
                elif choice8.strip().lower() == ("stay"):
                    print('"You\'ve already come this far, human. Get the lead out!"')
                    print("_________________________________________________________")
                else:
                    print("Try again, this is a simple text game.")
        elif choice7.lower().strip() == ("leave it"):
            print("Don't be a dope. You'll obviously need that!")
            print("____________________________________________")
        else:
            print("Try again, this is a simple text game.")

    # Room5
    while loop == 6:
        if loop == 6:
            print("___________________________________________________________________")
            print(
                "You keep going down into utter darkness. You can't see a thing! Scary."
            )
            print('"Wait, human, I got you."')
            print("The fairy glows and you are able to see. Magic? Far out.")
            print(
                "You keep descending and find yourself in a vast, underground cavern. Echo!"
            )
            print("You keep going until you see an old trunk with a lock on it.")
            print('"Unlock the trunk!"')
            choice9 = input("Unlock or naw? ")
        if choice9.strip().lower() == ("unlock"):
            print(
                "_______________________________________________________________________."
            )
            print(
                "You open the trunk and find a wicked looking sword and shield inside. Cool."
            )
            print(
                "\"What are you waiting for human? You'll need those if you're going to fight the evil wizard!\""
            )
            loop = 12
            while loop == 12:
                choice10 = input("Take or leave? ")
                if choice10.strip().lower() == ("take"):
                    loop = 7
                elif choice10.strip().lower() == ("leave"):
                    print(
                        "The fairy takes a deep breath of exasperation, waiting for you to make the right decsion."
                    )
                    print(
                        "_______________________________________________________________________________________"
                    )
                else:
                    print("Try again, this is a simple text game.")
        elif choice9.strip().lower() == ("naw"):
            print(
                "The fairy looks at you like you're an idiot. You really don't think you'll need what's inside? Guess again."
            )
            print(
                "______________________________________________________________________________________________________"
            )
        else:
            print("Try again, this is a simple text game.")

    # Room6
    while loop == 7:
        if loop == 7:
            print("_______________________________________________________")
            print("You take the sword and shield and continue on your way.")
            print("You see a door in front of you and you open it.")
            print("You are in a tiny room. It looks like a closet.")
            print(
                "Across the room, almost within arm's length, you see a door. You approach the door."
            )
            print(
                '"Wait, human! The evil wizard is on the other side! Drink the elixir!"'
            )
            choice11 = input("Drink or naw? ")
        if choice11.strip().lower() == ("drink"):
            loop = 8
        elif choice11.strip().lower() == ("naw"):
            print('"Dammit, human! We\'ve come too far for you to screw this up now!"')
            print(
                "____________________________________________________________________"
            )
        else:
            print("Try again, this is a simple text game.")

    # Room7
    while loop == 8:
        if loop == 8:
            print("__________________________________________________________")
            print("You start to drink the elixir and immediately spit it out.")
            print("You look at the bottle: Kombucha?! That stupid hipster!")
            print("You glare at the fiary.")
            print("\"Hey, don't blame me, man. I'm just a part of the program.\"")
            print("You sigh, and open the door.")
            print(
                "Inside is an evil wizard, laughing maniacally. A beautiful princess is chained to the wall."
            )
            print(
                'The wizard turns to you. "What is this? An intruder? Not on my watch!"'
            )
            print("The wizard starts to transform into a dragon.")
            print('"Don\'t just stand there, human, attack!"')
            print("_________________________________________")
            choice12 = input("Attack or panic? ")
        if choice12.lower().strip() == ("panic"):
            print("The wizard turns into a massive dragon and eats you. Damn.")
            panic1_inp = input("Start over or no? Y/N ")
            if panic1_inp.strip().lower() == ("n"):
                exit()
            elif panic1_inp.strip().lower() == ("y"):
                loop = 1
            else:
                print("Try again, this is a simple text game.")
        elif choice12.lower().strip() == ("attack"):
            print("______________________")
            print("You attack the wizard!")
            print(
                "You interrupt his transformation spell and you do battle with a hideous half-man, half-dragon creature."
            )
            print(
                "After hours of grueling combat, you overpower the wizard and plunge your sword into his face! Gnarly."
            )
            print(
                "The wizard screams in agony and melts into a puddle of maggots as he dies. Gross."
            )
            print("You look to the princess on the wall.")
            print(
                '"My hero! You have saved me! My father, the Wise King, will give you his kingdom and my hand in marriage for this act of heroism!"'
            )
            print(
                '"Oh brave hero, oh valient savior, I pledge myself to be your loyal and loving wife if you will free me from this place of evil!"'
            )
            loop = 13
        else:
            print("Try again, this is a simple text game.")
    while loop == 13:
        if loop == 13:
            choice13 = input("Free her or naw? ")
        if choice13.lower().strip() == ("naw"):
            print(
                "___________________________________________________________________________________"
            )
            print(
                "You wander away while the damsel in distress cries for help. What kind of bum are you? Free her!"
            )
        elif choice13.lower().strip() == ("free her"):
            print("_________________________________________________")
            print("You free the princess and escape the evil castle.")
            print(
                "As you ride away on your trusty steed into the sunset with the beautiful princess, you reflect back on your adventures."
            )
            print(
                "You take pride in the fact that you have confronted the forces of chaos and tyranny and have emerged on top, a bigger and better man."
            )
            choice14 = input(
                "That was fun, wasn't it? Want to play again? Y/N ")
            if choice14.strip().lower() == ("y"):
                loop = 1
            elif choice14.strip().lower() == ("n"):
                exit()
            else:
                print("Try again, this is a simple text game.")
        else:
            print("Try again, this is a simple text game.")
