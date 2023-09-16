#!/usr/bin/env python

import random
import sys


class InvalidRollError(Exception):
    "Raised when the player input value is greater than 2 or less than 0"
    pass

# get player input
try:
    print("ROCK PAPER SCISSOR GAME")
    print("ENTER 0 FOR ROCK, 1 FOR PAPER, 2 FOR SCISSORS")
    player_input = input("ENTER A NUMBER: ")
    player_num = int(player_input)
    if player_num > 2 or player_num < 0:
        raise InvalidRollError
except NameError:
    player_input = 0
    print("OH NO THATS NOT A NUMBER. PLAYER INPUT IS NOW 0")
except InvalidRollError:
    print("You stinky cheater!")
    sys.exit(0)
except:
    print("Something terrible happened")

# get npc input
npc_num = random.randrange(3)

# debug msgs
# player_input = 2
# npc_num = 1
print(f"PLAYER = {player_input}")
print(f"NPC = {npc_num}")


tie_msg = "Tie game!"
lose_msg = "Sorry :( You lost this one"
win_msg = "Congratulations! You won"

# ROCK CONDITIONS
if npc_num == 0:
    if player_num == 0:
        print(tie_msg)
    elif player_num == 1:
        print(lose_msg)
    else:
        print(win_msg)
# PAPER CONDITIONS
elif npc_num == 1:
    if player_num == 1:
        print(tie_msg)
    elif player_num == 2:
        print(lose_msg)
    else:
        print(win_msg)
# SCISSOR CONDITIONS
elif npc_num == 2:
    if player_num == 2:
        print(tie_msg)
    elif player_num == 1:
        print(lose_msg)
    else:
        print(win_msg)
else:
    raise InvalidRollError
