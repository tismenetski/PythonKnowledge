
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


bidders = {}
on  = True
highest_bid = 0
winner = ""
print(logo)

while on:
    name = input("Please enter your name: ")
    bid = int(input("Please enter the bid sum: $"))
    bidders[name] = bid
    if bid > highest_bid:
        highest_bid = bid
        winner = name
    yes_or_no_continue = input("Are there any other bidders in the room? (y/n)")
    if yes_or_no_continue == 'y':
        clear_screen()
    else:
        on = False

print(f"The winner is {winner} with the sum ${highest_bid}")