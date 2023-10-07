import random
from art import logo
# from replit import clear : "this is to clear console in replit"

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def check_black_jack(computer_score, user_score):
    if computer_score == 21 and user_score == 21:
        print("both you and the dealer have  scored a blackjack, it's a draw.")
        return 1
    elif computer_score == 21:
        print("dealer has a blackjack, you lose")
        return 1
    elif user_score == 21:
        print(" you have a blackjack, you win.")
        return 1
    else:
        return 0


def get_score(cards):
    if len(cards) > 2 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def check_win(computer_score, user_score):
    if computer_score > 21 and user_score > 21:
        return " both you and the dealer bust, it's a draw."
    elif user_score > 21:
        return "It's a bust, and you lose"
    elif computer_score > 21:
        return "The dealer has busted, and you win"
    elif user_score == computer_score:
        return f" both you and the dealer have a score of {computer_score}, it's a draw."
    elif computer_score > user_score:
        return f"you lose"
    elif user_score > computer_score:
        return f"you win"


def play():
    should_play = False
    if (input("Do you want to play blackjack? Type 'y' to play or 'n' to exit: ")).lower() == 'y':
        # clear(): "use in replit"
        print(logo)
        should_play = True
        players_hand = []
        dealers_hand = []
        for n in range(2):
            dealers_hand.append(deal_card())
            players_hand.append(deal_card())
        dealer_score = get_score(dealers_hand)
        player_score = get_score(players_hand)
        print(f"You hand: {players_hand}, current score: {player_score}")
        print(f"Dealer's first hand: {dealers_hand[0]}")
        score = check_black_jack(dealer_score, player_score)
        if score == 0:
            while True:
                choice = (input("Type 'y' to get another card or 'n' to pass: ")).lower()
                print("\n----------------------------------------------------")
                if choice == 'y':
                    players_hand.append(deal_card())
                    player_score = get_score(players_hand)
                    if player_score >= 21: break
                    print(f"Your cards: {players_hand}, current score: {player_score}")
                    print(f"Dealer's first card: {dealers_hand[0]}")
                elif choice == 'n':
                    break
            while dealer_score < 17 and player_score < 21:
                dealers_hand.append(deal_card())
                dealer_score = get_score(dealers_hand)
            result = check_win(dealer_score, player_score)
            print(result)
        print(f"your final hand: {players_hand}, final score: {player_score}")
        print(f"dealer's final hand: {dealers_hand}, final score: {dealer_score}")
        if should_play: play()
    else:
        return


play()
