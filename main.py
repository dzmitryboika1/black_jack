from random import shuffle

from art import logo
from deck import card_values


def play_blackjack():
    """start and end game"""
    print(logo)
    end_game = False
    while not end_game:
        deck = card_values[:]
        player_hand, dealer_hand = deal_first_cards(deck)
        deck = deck[4:]
        print_first_hands(player_hand, dealer_hand)
        player_points, dealer_points = counting_points(player_hand, dealer_hand)
        check_result(player_points, dealer_points)

        if input("Wanna play again?").lower() == 'n':
            end_game = True
        else:
            play_blackjack()


def deal_first_cards(new_deck):
    """dealing and printing first hands"""
    shuffle(new_deck)
    player_cards = [new_deck[0], new_deck[2]]
    dealer_cards = [new_deck[1], new_deck[3]]
    return player_cards, dealer_cards


def print_first_hands(player_hand, dealer_hand):
    """printing first player's and dealer's first hands(one dealer's card is hidden)"""
    displayed_player_cards = ""
    for card in player_hand:
        for key in card:
            displayed_player_cards += key
    print(f"Your cards: {displayed_player_cards}")
    displayed_dealer_card = ""
    for card_key in dealer_hand[1]:
        displayed_dealer_card += card_key
    print(f"Dealer's cards: 🂠{displayed_dealer_card}")


def counting_points(player_hand, dealer_hand):
    player_points = 0
    for card in player_hand:
        player_points += sum(card.values())
    dealer_points = 0
    for card in dealer_hand:
        dealer_points += sum(card.values())
    return player_points, dealer_points


def take_one_card():
    pass


def check_result(player_points, dealer_points):
    if player_points == 21 and dealer_points != 21:
        print("Blackjack! You win!")
    elif player_points == 21 and dealer_points == 21:
        print_first_hands(player_hand, dealer_hand)  # нужно как то раскрыть карты дилера


if input("Would you like to play Blackjack? yes/no: ").lower() == "yes":
    play_blackjack()
