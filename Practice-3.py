import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = int(input())

if choice == 0:
    print('''
    Rock
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
      ''')
elif choice == 1:
    print('''
    Paper
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
    ''')
elif choice == 2:
    print('''
    Scissors
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
    ''')

bot_input = random.randint(0,2)

print("Computer choose:")

if bot_input == 0:
    print('''
    Rock
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
      ''')
elif bot_input == 1:
    print('''
    Paper
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
    ''')
elif bot_input == 2:
    print('''
    Scissors
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
    ''')
    
if choice == bot_input:
    print("It's a draw.")
elif choice == 0 and bot_input == 1:
    print("Computer won.")
elif choice == 0 and bot_input == 2:
    print("You won!")
elif choice == 1 and bot_input == 0:
    print("You won!")
elif choice == 1 and bot_input == 2:
    print("Computer won.")
elif choice == 2 and bot_input == 0:
    print("Computer won")
elif choice == 2 and bot_input == 1:
    print("You won!")
