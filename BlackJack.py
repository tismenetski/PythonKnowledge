import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]  # The deck is endless


def deal_card():
    """Function deals a card to a player"""
    return random.choice(cards)

def calculate_score(player_cards):
    """Function takes a list and calculates the score"""
    sum = 0
    check_eleven = False

    for card in player_cards:
        if card == 11:
            check_eleven = True

    for card in player_cards:
        sum+= card

    if sum > 21 and check_eleven == True:
        player_cards.append(1)
        player_cards.remove(11)

    if sum == 21:
        return 0

    return sum

def compare(user_cards,cpu_cards):

    player_sum = 0
    cpu_sum = 0
    for card in user_cards:
        player_sum+=card
    for card in cpu_cards:
        cpu_sum += card

    if (player_sum == 0 and cpu_sum == 0) or ((player_sum == cpu_sum) and (player_sum <21)):
        return "draw"
    elif player_sum == 0 and cpu_sum != 0:
        return "player wins"
    elif cpu_sum == 0 and player_sum != 0:
        return "cpu wins"
    elif player_sum > 21:
        return "cpu wins"
    elif (player_sum <= 21) and (cpu_sum < player_sum):
        return "player wins"
    elif (cpu_sum <= 21) and (cpu_sum > player_sum):
        return "cpu wins"
    elif player_sum <=21 and cpu_sum > 21:
        return "player wins"


print("Welcome to python blackjack game!")


def game():
    """Function handles the game, first goes the player , then the cpu , then decision of game winner"""
    game_state = True
    player_cards = []
    #player_sum = 0
    cpu_cards = []
    #cpu_sum = 0
    while game_state:

        player_cards.append(deal_card())
        player_cards.append(deal_card())
        print(player_cards)

        while input("Would you like to draw another card? (y/n)")=='y':
            player_cards.append(deal_card())
            print(player_cards)

        while calculate_score(cpu_cards) < 17:
            cpu_cards.append(deal_card())
            print(cpu_cards)

        result = compare(player_cards,cpu_cards)
        print(f"The result is {result}")

        if input("Would you like to play again? (y/n)") == 'y':
            game()  # Recursive call to restart the game
        else:
            game_state = False  # end game


game()