import random


def get_choices():
    player_choices = input("enter a choice(rock,paper,scissors:")
    options = ["rock", "paper", "scissors"]
    computer_choices = random.choice(options)
    choices = {"player": player_choices, "computer": computer_choices}
    return choices


response = get_choices()
print(response)


def ckeck_win(player, computer):
    if player== computer :
        return "It's a tie"

