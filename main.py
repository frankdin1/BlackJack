import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
player_score = 0
dealer_score = 0


def initiate_game():
    play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if play_game == 'y':
        player_scores = initial_deal()
        return player_scores


# function to deal cards at beginning of the game
def initial_deal():
    # pick two random cards from the deck for the user and display them
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    p_score = player_cards[0] + player_cards[1]
    print(f"\tYour cards: {player_cards}, current score: {p_score}")

    # pick two random cards from the deck for the computer, but only reveal the computer's first card.
    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    d_score = dealer_cards[0] + dealer_cards[1]
    print(f"\tComputer's first card: {dealer_cards[0]}")

    return p_score, d_score


# Store returned values in variables created to store player and computer scores
scores = initiate_game()
player_score += scores[0]
dealer_score += scores[1]

if player_score == 21 and dealer_score != 21:
    print("You won a BlackJack.")
elif player_score == 21 and dealer_score == 21:
    print("You and the Computer both scored BlackJack.")
elif player_score < 21 and dealer_score == 21:
    print("You lost.")

while (player_score < 21):
    pick_another_card = input("Type 'y' to pick another card or 'n' to pass: ")
    if pick_another_card == 'y':
        player_cards.append(random.choice(cards))
        player_score += player_cards[-1]
        print(f"\tYour cards: {player_cards}, current score: {player_score}")
        print(f"\tComputer's first card: {dealer_cards[0]}")
    elif pick_another_card == 'n':
        print(f"\tYour final hand: {player_cards}, final score: {player_score}")
        print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_score}")
        if player_score < 21 and dealer_score > player_score:
            print("You lose")
        elif player_score < 21 and player_score > dealer_score:
            print("You win")
        elif player_score < 21 and dealer_score == player_score:
            print("It's a draw.")
        break
if player_score > 21:
    print(f"\tYour final hand: {player_cards}, final score: {player_score}")
    print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_score}")
    print("You went over. You lose.")
