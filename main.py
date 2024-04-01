import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []
player_score = 0
computer_score = 0
play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

if play_game == 'y':
    #pick two random cards from the deck for the user and display them
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    player_score = player_cards[0] + player_cards[1]
    print(f"\tYour cards: {player_cards}, current score: {player_score}")


    #pick two random cards from the deck for the computer, but only reveal the computer's first card.
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    computer_score = computer_cards[0] + computer_cards[1]
    print(f"\tComputer's first card: {computer_cards[0]}")

while (player_score < 21):
    pick_another_card = input("Type 'y' to pick another card or 'n' to pass: ")
    if pick_another_card == 'y':
        player_cards.append(random.choice(cards))
        player_score += player_cards[-1]
        print(f"\tYour cards: {player_cards}, current score: {player_score}")
        print(f"\tComputer's first card: {computer_cards[0]}")
    elif pick_another_card == 'n':
        print(f"\tYour final hand: {player_cards}, final score: {player_score}")
        print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
