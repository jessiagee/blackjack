# player needs to track their money

global hand
global bankroll


def bet(new_game):
    global bankroll

    if new_game:
        bankroll = Bankroll()
    else:
        bankroll.amount_bet = 0

    while bankroll.amount_bet <= 0:
        bet_amt = int(input("How much do you want to bet? "))

        if bankroll.bet_amt(bet_amt):
            return


def win():
    bankroll.won_bet()


def lose():
    bankroll.lost_bet()


class Bankroll:
    def __init__(self, amount_bet=0, balance=100):
        self.balance = balance
        self.amount_bet = amount_bet

    def __str__(self):
        return f'Bankroll balance: ${self.balance}'

    def bet_amt(self, bet_amt):
        if bet_amt <= self.balance:
            self.amount_bet = bet_amt
            print(f"You are betting ${self.amount_bet}!\n")
        else:
            print(f"Bankroll ${self.balance} cannot support ${bet_amt} bet, try again.")

        return self.amount_bet > 0

    def won_bet(self):
        self.balance += self.amount_bet
        print(f"Congratulations on winning ${self.amount_bet}! Your bankroll is now ${self.balance}!")

    def lost_bet(self):
        print("Better luck next time!")
        if self.balance >= self.amount_bet:
            self.balance -= self.amount_bet
            print(f"Your bankroll is now ${self.balance} after a ${self.amount_bet} loss.")
