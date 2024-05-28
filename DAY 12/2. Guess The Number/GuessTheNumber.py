from random import randint
import art
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
#Function to check user's guess against actual number
def check_answer(guess,answer,turns):
  '''Checks answer against guess, returns the number of turns remaining'''
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}")

#Set difficulty level
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  #Choosing a number between 1 to 100
  print(art.logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  answer = randint(1,100)
  
  
  #Let the user guess a number
  turns = set_difficulty()
  
  #Repeat the guessing functionality if they get wrong
  guess = 0
  while guess!= answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))
    
    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("You've run out of guesses, You Lose.")
      return
    elif guess != answer:
      print("Guess again!")
    
    #Track the number of turns and reduce by 1 if they get it wrong
    

game()
  

  
  

  