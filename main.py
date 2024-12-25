name = input("Type your name: ")
print("Welcome!", name, "to your adventure")

answer = input("You have stumbled upon two different paths, you must make a choice now to go left or right."
               " Choose wisely!" ).lower()
# user amswers
if answer == "left":
    answer = input("You have discovered a river, you either swim across or walk around it. Type walk to walk and swim to swim: ")

    if answer == "swim":
        print("Unfortunately for you the water was infested with piranhas...you never stood a chance :/")
    elif answer == "walk":
        print("During your walk, the aliens abducted you in a space ship (not good). You lost.")
    else:
        print("Not a valid option. You lose! :P")
# right side of game
elif answer == "right":
    answer = input("You have encountered a rabid racoon. You can either walk around him, shoo him away with a stick, or kick him.  "
                   "Type walk to walk, stick to shoo or kick to kick: ")
# main decisions on right side
    # answers: walk - lose, stick - win, kick - win.
    if answer == "walk":
        print("The racoon caught you trying to sneak by! You ran away only to get bit on the ankle :( you lost (and probably have rabies).")
    elif answer == "stick":
        print("The racoon latched on to the stick giving you enough time to sneak by him! Good job!!")
        answer = input("After dealing with the racoon, you meet a strange figure who hands you a key. Do you take it? (yes/no): ")
        if answer == "yes":
            print("You took the key, after this you were given a locked box that had a gold bar in it! YOU WIN!!!!!")
        elif answer == "no":
            print("You passed on the key, which means you lost a chance to win a gold bar :( womp womp, you lost.")
    elif answer == "kick":
        print("You sent that racoon 68 yards downfield, NFL teams are now scouting you. Good job!!")
        answer = input("After kicking the racoon you meet a strange figure who hands you a key. Do you take it? (yes/no): ")
        if answer == "yes":
            print("You took the key, after this you were given a locked box that had a gold bar in it! YOU WIN!!!!!")
        elif answer == "no":
            print("You passed on the key, which means you lost a chance to win a gold bar :( womp womp, you lost.")

else:
    print("Not a valid option. You lose! :P")