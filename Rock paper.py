import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [Rock, Paper, Scissors]

User_choice = int(input("Please enter your choice (0 Rock, 1 Paper, and 2 for Scissors) \n"))

if User_choice < 0 or User_choice > 2:
    print("You entered an invalid number")
else:
    print(game_images[User_choice])

    Computer_choice = random.randint(0, 2)
    print("Computer choice:")
    print(game_images[Computer_choice])

    if User_choice == Computer_choice:
        print("It's a draw")
    elif (User_choice == 0 and Computer_choice == 2) or \
         (User_choice == 1 and Computer_choice == 0) or \
         (User_choice == 2 and Computer_choice == 1):
        print("You won!")
    else:
        print("You lost!")
