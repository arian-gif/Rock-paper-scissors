rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game = [rock, paper,scissors]
num = random.randint(0,2)

computer = game[num]
choice = int(input("What do you chose? Type 0 for rock, 1 for paper and 2 for scissios:\n"))

your_choice = game[choice]

print("\nYou chose:")
print(your_choice)
print("Computer chose:")
print(computer)

if your_choice == computer:
    print("It's a tie!")
elif (choice == 0 and num == 2) or (choice == 1 and num == 0) or (choice == 2 and num == 1):
    print("You win!")
else:
    print("You lose!")
