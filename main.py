name = input("Type your name: ")
print("Welcome!", name, "to your adventure")

answer = input("You have stumbled upon two different paths, you must make a choice now to go left or right."
               " Choose wisely!").lower()
# user amswers
if answer == "left":
    answer = input("You have discovered a river, you either swim across or walk around it. Type walk to walk and swim to swim: ")

    if answer == "swim":
        print("Unfortunately for you the water was infested with piranhas...you never stood a chance :/")
    elif answer == "walk":
        print("During your walk, the aliens abducted you in a space ship (not good). You lost.")
    else:
        print("Not a valid option. You lose! :P")

elif answer == "right":
    answer = input("You have encountered a rabid racoon. You can either walk around him, shoo him away with a stick, or kick him.  "
                   "Type walk to walk, stick to shoo or kick to kick: ")

    if answer == "walk":
        print("The racoon caught you trying to sneak by! You ran way only to get bit on the ankle :( you lost.")
    elif answer == "stick":
        print("The racoon latched on to the stick giving you enough time to sneak by him! Good job!!")
    elif answer == "kick":
        print("You sent that racoon 68 yard downfield, NFL teams are now scouting you. Good job!!")
    else:
        print("Not a valid option. You lose! :P")

else:
    print("Not a valid option. You lose! :P")