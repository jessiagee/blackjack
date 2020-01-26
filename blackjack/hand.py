# -*- coding: utf-8 -*-
"""
A module for the Hand class
"""

import deck


class Hand:
    """ Represents the hand object """
    def __init__(self, cards, hidden=False):
        """
        Initializing the Hand class and its attributes.

        :param cards: the current deck of cards
        :param hidden: used if this is the dealer's HAND

        :type cards: a list of Card objects
        :type hidden: bool
        """
        self.cards = cards
        self.hidden = hidden
        # total number of points for the HAND
        self.points = 0

        for card in self.cards:
            self.points += card.points

    def __str__(self):
        """
        The string representation of the HAND

        :return: a string representation of the HAND
        """
        if self.hidden is False:
            return deck.ascii_version_of_card(*self.cards)

        return deck.ascii_version_of_hidden_card(*self.cards)

    def add_card(self, card):
        """
        Adds a Card object to the current HAND

        :param card: a card to add to the HAND
        :type card: a Card object
        """
        self.cards.append(card)
        self.points += card.points
