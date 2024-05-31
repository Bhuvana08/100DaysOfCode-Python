import random
from game_data import data
import art
from replit import clear


# Generate a random item from the game_data
def generate_random_data(data):
    return random.choice(data)


#Print fromat
def format_data(account,acc_name):
    account_name = account['name']
    account_desc = account['description']
    account_countr = account['country']
    
    print(
        f"Compare {acc_name} : {account_name}, a {account_desc}, from {account_countr}"
    )


#Compare the followers count
def compare_count(guess, A, B):
    if A['follower_count'] > B['follower_count']:
        return guess == 'A'
    else:
        return guess == 'B'


def game():
    print(art.logo)
    score = 0
    A = generate_random_data(data)
    B = generate_random_data(data)

    end_of_game = False
    while not end_of_game:
        A = B
        B = generate_random_data(data)

        while A == B:
            B = genearte_random_data(data)

        format_data(A,'A')
        print(art.vs)
        format_data(B,'B')

        guess = input("Who has more follower count ? Type 'A' or 'B' : ")

        is_correct = compare_count(guess, A, B)
        
        clear()
        print(art.logo)
        
        if is_correct:
            score += 1
            print(f"You are right! Current score :  {score}")
        else:
            
            print(f"Sorry, that's wrong. Final score :  {score}")
            
            
            end_of_game = True


if input("Do you want to play higher lower game ? Type 'Y' or 'N' : ") == 'Y':
    game()
