"""Simple version of rock paper and scissors."""
from random import choice

def normalize_user_name(name: str) -> str:
    """
    Simple function gets player name as input and capitalizes it.

    :param name: name of the player
    :return: A name that is capitalized.
    """
    a = name.capitalize()
    return a


def reverse_user_name(name: str) -> str:
    """
    Function that takes in name as a parameter and reverses its letters. The name should also be capitalized.

    :param name: name of the player
    :return: A name that is reversed.
    """
    a = name[::-1].capitalize()
    return a


def check_user_choice(choice: str) -> str:
    """
    Function that checks user's choice.

    The choice can be uppercase or lowercase string, but the choice must be
    either rock, paper or scissors. If it is, then return a choice that is lowercase.
    Otherwise return 'Sorry, you entered unknown command.'
    :param choice: user choice
    :return: choice or an error message
    """
    a = choice.lower()
    if a == "rock":
        return "rock"
    if a == "paper":
        return "paper"
    if a == "scissors":
        return "scissors"
    return "Sorry, you entered unknown command."


def determine_winner(name: str, user_choice: str, computer_choice: str, reverse_name: bool = False) -> str:
    """
    Determine the winner returns a string that has information about who won.

    You should use the functions that you wrote before. You should use check_user_choice function
    to validate the user choice and use normalize_user_name for representing a correct name. If the
    function parameter reverse is true, then you should also reverse the player name.
    NB! Use the previous functions that you have written!

    :param name:player name
    :param user_choice:
    :param computer_choice:
    :param reverse_name:
    :return:
    """
    b = check_user_choice(user_choice)
    c = check_user_choice(computer_choice)
    if (b == "Sorry, you entered unknown command." or c == "Sorry, you entered unknown command."):
        return "There is a problem determining the winner."
    a = name
    a = normalize_user_name(a)
    if (reverse_name is True):
        a = reverse_user_name(a)
    if((b == "rock" and c == "paper") or (b == "paper" and c == "rock")):
        result = "paper"
        if result == b:
            return (f"{a} had paper and computer had rock, hence {a} wins.")
        else:
            return (f"{a} had rock and computer had paper, hence computer wins.")
    elif((b == "rock" and c == "scissors") or (b == "scissors" and c == "rock")):
        result = "rock"
        if result == b:
            return (f"{a} had rock and computer had scissors, hence {a} wins.")
        else:
            return (f"{a} had scissors and computer had rock, hence computer wins.")
    else:
        result = "scissors"
        if result == b:
            return (f"{a} had scissors and computer had paper, hence {a} wins.")
        else:
            return (f"{a} had paper and computer had scissors, hence computer wins.")
    return (f"{a} had {b} and computer had {c}, hence it is a draw")


def play_game() -> None:
    """
    Enable you to play the game you just created.

    :return:
    """
    user_name = input("What is your name? ")
    play_more = True
    while play_more:
        computer_choice = choice(['rock', 'paper', 'scissors'])
        user_choice = check_user_choice(input("What is your choice? "))
        print(determine_winner(user_name, user_choice, computer_choice))
        play_more = True if input("Do you want to play more ? [Y/N] ").lower() == 'y' else False
    play_game()