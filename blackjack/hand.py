import deck


class Hand:
    def __init__(self, cards, hidden=False):
        self.cards = cards
        self.hidden = hidden
        self.points = 0

        for card in self.cards:
            self.points += card.points

    def __str__(self):
        if self.hidden is False:
            return deck.ascii_version_of_card(*self.cards)
        else:
            return deck.ascii_version_of_hidden_card(*self.cards)

    def add_card(self, card):
        self.cards.append(card)
        self.points += card.points
