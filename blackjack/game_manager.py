# -*- coding: utf-8 -*-
"""
The game manager for the blackjack game.  Handles creating the deck, distributing cards, and the
main game loop.
"""
import sys

import dealer
import deck
import player


def setup(new_game=True):
    """
    Sets the game up to be played. Creates the deck which shuffles the cards.
    Allows the player to place an initial bet after printing their current BANKROLL.
    Dealer than deals cards for both dealer and player and then the game starts.

    :param new_game: is this a new game?
    :type new_game: bool
    """
    game_deck = deck.create()
    player.bet(new_game)
    dealer.deal_start_cards(game_deck)

    play_game(game_deck)


def play_game(game_deck):
    """
    The game loop

    While the player has less than 21 points, they are able to hit, stand, or double.
    If the player goes over 21 points in this loop, they bust and lose.
    If a player hits 21 points in this loop, they get blackjack and win.

    Once determined if the player wins or loses, they are allowed to replay if they still
    have money in their BANKROLL.

    :param game_deck: the current deck of cards
    :type game_deck: a list of Card objects
    """
    player_points = player.HAND.points
    dealer_points = dealer.HAND.points

    while player_points < 21:
        print_hands()

        command = get_next_command()

        if command == 'HIT':
            player_points = hit(game_deck)
        elif command == 'STAND':
            stand(game_deck, player_points, dealer_points)
            return
        elif command == 'DOUBLE':
            double(game_deck, dealer_points)
            return
        else:
            print(f"Command {command} not recognized")

    if player_points > 21:
        print(f"Busted!\n")
        player.lose()
    else:
        player.win()

    replay()


def get_next_command():
    """
    Asks players to hit, stand, or double, validates the input, and returns
    the command.

    :returns: (string) command: HIT, STAND, or DOUBLE
    """
    while True:
        command = input("Do you want to hit, stand, or double?  ")
        command = command.upper()

        if command not in ('HIT', 'STAND', 'DOUBLE'):
            print(f"The command {command} is incorrect! Please re-enter a correct command.\n")
            continue

        break

    return command


def determine_winner(game_deck, player_points, dealer_points):
    """
    Dealer gives themselves cards until they reach 17 and
    then the total player and dealer points are compared.

    :param game_deck: the current deck of cards
    :param player_points: the player's current points
    :param dealer_points: the dealer's current points
    :type game_deck: list of Card objects
    :type player_points: int
    :type dealer_points: int
    """
    while dealer_points <= 17:
        dealer.deal_single_card(game_deck, dealer=True)
        dealer_points = dealer.HAND.points
        print_hands()

    if player_points > dealer_points or dealer_points > 21:
        player.win()
    elif dealer_points == player_points:
        print(f"Player and dealer tied! No money won or lost!\n")
    else:
        player.lose()

    replay()


def hit(game_deck):
    """
    Player gets another card added to their HAND and their points increase.

    :param game_deck: the current deck of cards
    :type game_deck: list of Card objects

    :returns: (int) player_points: the number of points the player has in their HAND
    """
    dealer.deal_single_card(game_deck)
    print_hands()

    player_points = player.HAND.points
    return player_points


def stand(game_deck, player_points, dealer_points):
    """
    Player will get no more cards, dealer will reveal their cards,
     and a winner will be determined from points after dealer hits 17.

    :param game_deck: the current deck of cards
    :param player_points: the current points of the player
    :param dealer_points: the current points of the dealer
    :type game_deck: list of Card objects
    :type player_points: int
    :type dealer_points: int
    """
    dealer.reveal_cards()
    print_hands()

    determine_winner(game_deck, player_points, dealer_points)


def double(game_deck, dealer_points):
    """
    Doubles the player's bet, gives them one more card, and then stands.

    :param game_deck: the current deck of cards
    :param dealer_points: the number of points the dealer has
    :type game_deck: list of Card objects
    :type dealer_points: int
    """
    player.double()
    player_points = hit(game_deck)
    stand(game_deck, player_points, dealer_points)


def replay():
    """
    Replays the game depending on player input if they still have
    money in their BANKROLL
    """
    if player.BANKROLL.balance <= 0:
        print(f"\nYou've run out of money! Time to call it a day!\n")
        sys.exit()

    user_input = 'Do you want to play again? [Y, N]: '
    valid_key_1 = 'Y'
    valid_key_2 = 'N'

    response = validate_input(user_input, valid_key_1, valid_key_2)

    if response == 'Y':
        setup(new_game=False)
    else:
        print(f"Your final bankroll was ${player.BANKROLL.balance}!")
        sys.exit()


def validate_input(user_input, valid_key_1, valid_key_2):
    """
    Validates the player's input.

    :param user_input: the user's input
    :param valid_key_1: the key to check for validity
    :param valid_key_2: the key to check for validity
    :type user_input: string
    :type valid_key_1: string
    :type valid_key_2: string

    :return: to_validate (string)
    """

    while True:
        to_validate = input(user_input)
        to_validate = to_validate.upper()

        if to_validate in (valid_key_1, valid_key_2):
            return to_validate

        print("Incorrect option! Try again.")
        continue


def print_hands():
    """
    Prints out the player's and dealer's HANDs
    """
    print("=" * 10 + " DEALER " + "=" * 10)
    print(dealer.HAND)
    print("=" * 10 + " PLAYER " + "=" * 10)
    print(player.HAND)


if __name__ == "__main__":
    setup()
