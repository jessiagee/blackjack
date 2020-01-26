# tracks how many cards are dealt and when they are dealt
from blackjack.hand import Hand
import player

global hand


def deal_start_cards(deck):
    global hand
    hand = Hand([deck.pop(), deck.pop()], True)

    player.hand = Hand([deck.pop(), deck.pop()])


def deal_single_card(deck, dealer=False):
    global hand

    if dealer is True:
        hand.add_card(deck.pop())
    else:
        player.hand.add_card(deck.pop())


def reveal_cards():
    global hand

    hand = Hand(hand.cards)
