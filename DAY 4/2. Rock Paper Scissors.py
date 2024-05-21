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

#Write your code below this line 👇
import random
items = [rock,paper,scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
print("You choose : \n")
print(items[user_input])

computer_choose = random.randint(0,2)
print("Computer choose: \n")
print(items[computer_choose])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_input == computer_choose:
    print("It's a draw.")
elif user_input == 0 and computer_choose == 1:
    print("You lose")
elif user_input == 1 and computer_choose == 2:
    print("You lose")
else:
    print("You win!")