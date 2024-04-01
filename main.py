import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []

play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
if play_game == 'y':

    #pick two random cards from the deck for the user and display them
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    print(player_cards)

    #pick two random cards from the deck for the computer, but only reveal the computer's first card.
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    print(computer_cards)