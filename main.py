from random import shuffle

from art import logo
from deck import card_values


def play_blackjack():
    """the main function which start and end game"""
    print(logo)
    end_game = False
    while not end_game:
        if input("Wanna play again").lower() == 'n':
            end_game = True
        else:
            play_blackjack()


def deal_first_cards():
    new_deck = card_values[:]
    shuffle(new_deck)
    player_cards = [new_deck[0], new_deck[2]]
    displayed_player_card = ""
    for card in player_cards:
        for key in card:
            displayed_player_card += key
    print(f"Your cards: {displayed_player_card}")
    computer_cards = [new_deck[1], new_deck[3]]
    displayed_computer_card = ""
    for key in computer_cards[1]:
        displayed_computer_card += key
    print(f"Computer cards: 🂠{displayed_computer_card}")


deal_first_cards()
