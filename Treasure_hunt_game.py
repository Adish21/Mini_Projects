print("Welcome to my world")
print("This is a simple treasure hunt where you have to find treasue")
print("Let's start!")

choice_1 = input('Choose a direction you want from "right" and "left".\n').lower()

if choice_1 == "right":
    choice_2 = input('wwlcome to stage 2 you have a choice! Do you wanna "swim" or "stay"\n').lower()
    if choice_2 == "stay":
        choice_3 = input('This is a final stage! You can see a house with 3 doors "Red","Blue" and "Yellow". Please choose one1 \n').lower()
        if choice_3 == "red":
            print("Oops wrong door it is full of fire.")
        elif choice_3 == "blue":
            print("This is treasure full of gold! you are winner.")
        elif choice_3 == "yellow":
            print("A dragon is waiting for you in baby.")
        else:
            print("Demon king swallowed you for wrong input")
    else:
        print("You didn't stay in the island to find the treasure!")
else:
    print("You are out from stage 1")