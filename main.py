import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []


def blackjack(p_score, d_score):
    if p_score == 21 and d_score != 21:
        print("You won a BlackJack.")
    elif p_score == 21 and d_score == 21:
        print("You and the Computer both scored BlackJack.")


def subsequent_deal(p_score, d_score):
    while p_score < 21:
        pick_another_card = input("Type 'y' to pick another card or 'n' to pass: ")
        if pick_another_card == 'y':
            player_cards.append(random.choice(cards))

            if player_cards[-1] == 11:
                if p_score + player_cards[-1] > 21:
                    player_cards[-1] = 1
            p_score += player_cards[-1]

            print(f"\tYour cards: {player_cards}, current score: {p_score}")
            print(f"\tComputer's first card: {dealer_cards[0]}")
        elif pick_another_card == 'n':
            print(f"\tYour final hand: {player_cards}, final score: {p_score}")
            print(f"\tComputer's final hand: {dealer_cards}, final score: {d_score}")
            break
        elif p_score >= 21:
            break
    return p_score, d_score


def play():
    play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if play_game == 'y':
        scores = initial_deal()
        player_score = scores[0]
        dealer_score = scores[1]

        if player_score == 21 or dealer_score == 21:
            blackjack(player_score, dealer_score)
        elif player_score < 21:
            scores = subsequent_deal(player_score, dealer_score)
            player_score = scores[0]
            dealer_score = scores[1]
            if player_score < 21:
                if player_score < dealer_score < 21: # dealer_score > player_score and dealer_score < 21
                    print("You lose")
                elif (player_score > dealer_score) or dealer_score > 21:
                    print("You win")
                elif player_score == dealer_score:
                    print("It's a draw.")
            elif player_score == 21 or dealer_score == 21:
                blackjack(player_score, dealer_score)
            elif player_score > 21:
                print(f"\tYour final hand: {player_cards}, final score: {player_score}")
                print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_score}")
                print("You went over. You lose.")
        player_cards.clear()
        dealer_cards.clear()
        play()
    elif play_game == 'n':
        return

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


# Add function to change 11 to 1 if 11 will take player over 21

play()
