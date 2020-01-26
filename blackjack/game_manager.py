# game flow is this
#
# create a deck of cards, shuffle that deck
# player places a bet
# dealer deals themself two cards (one face up and one face down) and the player two cards (both face down)
# player decides whether to hit, stand, double, or split
# loops until player wins or loses
# reset with new shuffle

import dealer
import deck
import player


def setup(new_game=True):
    """
    Sets the game up to be played
    """
    game_deck = deck.create()
    player.bet(new_game)
    dealer.deal_start_cards(game_deck)

    play_game(game_deck)


def play_game(game_deck):
    player_points = player.hand.points
    dealer_points = dealer.hand.points

    while player_points < 21:
        print_hands()

        command = get_next_command()

        if command == 'HIT':
            dealer.deal_single_card(game_deck)
            player_points = player.hand.points
        elif command == 'STAND':
            dealer.reveal_cards()
            determine_winner(game_deck, player_points, dealer_points)
            break
        elif command == 'DOUBLE':
            """The player is allowed to increase the initial bet by up to 100% in exchange for committing to stand after 
            receiving exactly one more card. The additional bet is placed in the betting box next to the original bet. 
            Some games do not permit the player to increase the bet by amounts other than 100%. Non-controlling players 
            may double their wager or decline to do so, but they are bound by the controlling player's decision to take 
            only one card. """
        elif command == 'SPLIT':
            """If the first two cards of a hand have the same value, the player can split them into two hands, by moving 
            a second bet equal to the first into an area outside the betting box. The dealer separates the two cards and 
            draws an additional card on each, placing one bet with each hand. The player then plays out the two separate 
            hands in turn; except for a few restrictions, the hands are treated as independent new hands, with the player 
            winning or losing their wager separately for each hand. Occasionally, in the case of ten-valued cards, 
            some casinos allow splitting only when the cards have the identical ranks; for instance, a hand of 10-10 may 
            be split, but not one of 10-king. However, usually all 10-value cards are treated the same. Doubling and 
            further splitting of post-split hands may be restricted, and an ace and ten value card after a split are 
            counted as a non-blackjack 21. Hitting split aces is usually not allowed. Non-controlling players may follow 
            the controlling player by putting down an additional bet or decline to do so, instead associating their 
            existing wager with one of the two post-split hands. In that case they must choose which hand to play behind 
            before the second cards are drawn. Some casinos do not give non-controlling players this option, and require 
            that the wager of a player not electing to split remains with the first of the two post-split hands. """
        else:
            print(f"Command {command} not recognized")

    if player_points > 21:
        print(f"Busted!\n")
        player.lose()
    else:
        player.win()

    replay()


def get_next_command():
    while True:
        command = input("Do you want to hit, stand, double, or split?  ")
        command = command.upper()

        if command == "HIT" or command == "STAND" or command == "DOUBLE" or command == "SPLIT":
            break
        else:
            print(f"The command {command} is incorrect! Please re-enter a correct command.\n")
            continue

    return command


def determine_winner(deck, player_points, dealer_points):
    while dealer_points <= 17:
        dealer.deal_single_card(deck, dealer=True)
        dealer_points = dealer.hand.points
        print_hands()

    if player_points > dealer_points or dealer_points > 21:
        player.win()
    elif dealer_points == player_points:
        print(f"Player and dealer tied! No money won or lost!\n")
    else:
        player.lose()

    replay()


def split():
    pass


def double():
    pass


def replay():
    """
    Replays the game depending on player input
    """
    user_input = 'Do you want to play again? [Y, N]: '
    valid_key_1 = 'Y'
    valid_key_2 = 'N'

    response = validate_input(user_input, valid_key_1, valid_key_2)

    if response == 'Y':
        setup(new_game=False)
    else:
        print(f"Your final bankroll was ${player.bankroll.balance}!")
        exit()


def validate_input(user_input, valid_key_1, valid_key_2):
    """
    Validates the player's input.

    INPUT: user_input (string)
            valid_key_1 (string)
            valid_key_2 (string)

    OUTPUT: to_validate (string)
    """

    while True:
        to_validate = input(user_input)
        to_validate = to_validate.upper()

        if to_validate == valid_key_1 or to_validate == valid_key_2:
            return to_validate
        else:
            print("Incorrect option! Try again.")
            continue


def print_hands():
    print("=" * 10 + " DEALER " + "=" * 10)
    print(dealer.hand)
    print("=" * 10 + " PLAYER " + "=" * 10)
    print(player.hand)


if __name__ == "__main__":
    setup()
