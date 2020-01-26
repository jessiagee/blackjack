# -*- coding: utf-8 -*-
"""
The dealer for the blackjack game
"""

from blackjack.hand import Hand
import player

global HAND  # The dealer's global reference to the Hand class


def deal_start_cards(game_deck):
    """
    Deals the starting cards for the game.
    Sets the global HAND list for both dealer and player.
    Dealer's HAND has a hidden card at the start.

    :param game_deck: the current game deck
    :type game_deck: a list of Card objects
    """
    global HAND

    HAND = Hand([game_deck.pop(), game_deck.pop()], hidden=True)

    player.HAND = Hand([game_deck.pop(), game_deck.pop()])


def deal_single_card(game_deck, dealer=False):
    """
    Deals a single card to either dealer or player.

    :param game_deck: the current game deck
    :param dealer: whether or not this is to deal a single card to the dealer
    :type game_deck: a list of Card objects
    :type dealer: bool
    """
    global HAND

    if dealer is True:
        HAND.add_card(game_deck.pop())
    else:
        player.HAND.add_card(game_deck.pop())


def reveal_cards():
    """
    Recreates the dealer's cards so that the first is no longer hidden.
    """
    global HAND

    HAND = Hand(HAND.cards)
