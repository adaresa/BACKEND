from random import randint

"""
Prompt the user to select either Rock, Paper, or Scissors.
Instruct the computer to randomly select either Rock, Paper, or Scissors.
Compare the users choice and the computers choice.
Determine a winner (the user or the computer).
Inform the user who the winner is.
"""

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
  "tie" : "It's a tie!",
  "won" : "You WON!",
  "lost" : "You Lost!"
}


def decide_winner(user_choice, computer_choice):
  print("You selected: %s" % user_choice)
  print("Computer selected: %s" % computer_choice)
  if user_choice == computer_choice:
    print(message["tie"])
  elif user_choice == options[0] and computer_choice == options[2]:
    print(message["won"])
  elif user_choice == options[1] and computer_choice == options[0]:
    print(message["won"])
  elif user_choice == options[2] and computer_choice == options[1]:
    print(message["won"])
  else:
    print(message["lost"])


def play_RPS():
  user_choice = input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)


play_RPS()
