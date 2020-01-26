# -*- coding: utf-8 -*-
"""
The player for the blackjack game
"""

global HAND
global BANKROLL


def bet(new_game):
    """
    Asks the player to bet, validates they can afford the bet, prints their bet,
    and sends the bet to the Bankroll class.

    :param new_game: is this a new game?
    :type new_game: bool

    :return:
    """
    global BANKROLL

    if new_game:
        BANKROLL = Bankroll()
    else:
        BANKROLL.amount_bet = 0

    print(f"Starting bankroll {BANKROLL}.\n")

    while BANKROLL.amount_bet <= 0:
        try:
            bet_amt = int(input("How much do you want to bet? "))

            if bet_amt <= 0:
                print(f"The bet amount ${bet_amt} needs to be more than $0!")
                continue

            if BANKROLL.bet_amt(bet_amt):
                return
        except ValueError:
            print(f"The bet amount is incorrect! Please try again.")
            continue


def double():
    """
    Doubles the amount of money the player originally bet.
    """
    BANKROLL.bet_amt(BANKROLL.amount_bet * 2)


def win():
    """
    The player has won so the BANKROLL can add their bet to the balance.
    """
    BANKROLL.won_bet()


def lose():
    """
    The player has lost so the BANKROLL can withdraw their bet from the balance.
    """
    BANKROLL.lost_bet()


class Bankroll:
    """ Manager for the bankroll """
    def __init__(self, amount_bet=0, balance=100):
        """
        Initializes the Bankroll object

        :param amount_bet: how much money the player bet
        :param balance: how much money the player has
        :type amount_bet: int
        :type balance: int
        """
        self.balance = balance
        self.amount_bet = amount_bet

    def __str__(self):
        """
        A string representation of the Bankroll object

        :return: string
        """
        return f'balance: ${self.balance}'

    def bet_amt(self, bet_amt):
        """
        Checks to see if a player can bet the amount they're sending and if so sets the amount_bet
        to that amount

        :param bet_amt: the amount a player is betting

        :return: (bool) - whether or not a player has made a bet
        """
        if bet_amt <= self.balance:
            self.amount_bet = bet_amt
            print(f"You are betting ${self.amount_bet}!\n")
        else:
            print(f"Bankroll ${self.balance} cannot support ${bet_amt} bet, try again.")

        return self.amount_bet > 0

    def won_bet(self):
        """
        Adds the amount won with the bet to the Bankroll balance.
        """
        self.balance += self.amount_bet
        print(f"Congratulations on winning ${self.amount_bet}! "
              f"Your bankroll is now ${self.balance}!")

    def lost_bet(self):
        """
        Withdraws the amount lost from the Bankroll balance.
        """
        print("Better luck next time!")
        if self.balance >= self.amount_bet:
            self.balance -= self.amount_bet
            print(f"Your bankroll is now ${self.balance} after a ${self.amount_bet} loss.")
