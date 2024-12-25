name = input("Type your name: ")
print("Welcome!", name, "to your adventure")

answer = input("You have stumbled upon two different paths, you must make a choice now to go left or right."
               " Choose wisely!").lower()

if answer == "left":
    answer = input("You have discovered a river, you either swim across or walk around it. Type walk to walk and swim to swim: ")

    if answer == "swim":
        print()
    elif answer == "walk":
        print()
    else:
        print("Not a valid option. You lose! :P")

elif answer == "right":
    print()
else:
    print("Not a valid option. You lose! :P")