from replit import clear
import art
print(art.logo)
print("Welcome to secret auction program.")
end_of_auction = False
auction_dict = {}

while not end_of_auction:
    name = input("What is your name? : ")
    amount = int(input("What's your bid?: $"))

    auction_dict[name] = amount

    another_bidders = input('Are there any bidders? Type "yes" or "no".')
    if another_bidders == "yes":
        clear()
    else: 
        end_of_auction = True

max_bid = 0
winner_name = ""
for key in auction_dict:
    if auction_dict[key] > max_bid:
        max_bid = auction_dict[key]
        winner_name = key

print(f"The winner is {winner_name} with a bid of ${max_bid}.")