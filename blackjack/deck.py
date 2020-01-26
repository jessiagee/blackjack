# aces can be either 1 or 11 (player's choice)
# face cards are 10

# A "standard" deck of playing cards consists of 52 Cards in each of the 4 suits of Spades, Hearts, Diamonds,
# and Clubs. Each suit contains 13 cards: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King.

import random


def create():
    """
    Create the deck
    :return: a deck of cards (a list with tuples)
    """

    cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

    deck = []

    while True:
        ace_high_or_low = input("Should aces be high or low? [High, Low]  ")
        ace_high_or_low = ace_high_or_low.upper()

        if ace_high_or_low == "HIGH" or ace_high_or_low == "LOW":
            points = 11 if ace_high_or_low == 'HIGH' else 1
            print(f"Aces will be {ace_high_or_low} and count for {points} points!\n")
            break
        else:
            print(f"The input {ace_high_or_low} is incorrect! Please use high or low!")
            continue

    for suit in suits:
        for card in cards:
            pair = Card(suit, card, ace_high_or_low)
            deck.append(pair)

    shuffle_cards(deck)

    return deck


def shuffle_cards(deck):
    """
    Shuffle the deck
    :return:
    """

    random.shuffle(deck)

    return deck


"""
Code below is adapted from user Vader on StackOverflow
https://codereview.stackexchange.com/q/82103
"""

CARD = """\
┌─────────┐
│{}       │
│         │
│         │
│    {}   │
│         │
│         │
│       {}│
└─────────┘
""".format('{rank: <2}', '{suit: <2}', '{rank: >2}')

HIDDEN_CARD = """\
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
"""


def join_lines(strings):
    """
    Stack strings horizontally.
    This doesn't keep lines aligned unless the preceding lines have the same length.
    :param strings: Strings to stack
    :return: String consisting of the horizontally stacked input
    """
    lines = [string.splitlines() for string in strings]
    return '\n'.join(''.join(lines) for lines in zip(*lines))


def ascii_version_of_card(*cards):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :return: A string, the nice ascii version of cards
    """

    # we will use this to prints the appropriate icons for each card
    name_to_symbol = {
        'Spades': '♠',
        'Diamonds': '♦',
        'Hearts': '♥',
        'Clubs': '♣',
    }

    def card_to_string(card):
        # 10 is the only card with a 2-char rank abbreviation
        rank = card.rank if card.rank == '10' else card.rank[0]

        # add the individual card on a line by line basis
        return CARD.format(rank=rank, suit=name_to_symbol[card.suit])

    return join_lines(map(card_to_string, cards))


def ascii_version_of_hidden_card(*cards):
    """
    Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
    :param cards: A list of card objects, the first will be hidden
    :return: A string, the nice ascii version of cards
    """

    return join_lines((HIDDEN_CARD, ascii_version_of_card(*cards[1:])))


class Card:

    card_values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }

    def __init__(self, suit, rank, ace_high):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """

        self.suit = suit.capitalize()
        self.rank = rank

        ace_pair = {'Ace': 11} if ace_high == 'HIGH' else {'Ace': 1}
        self.card_values.update(ace_pair)

        self.points = self.card_values[rank]
