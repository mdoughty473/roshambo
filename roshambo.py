#!/usr/bin/env python

import random
import sys

class InvalidRPSError(Exception):
    "Raised when the player input value is rock, paper, or scissor"
    pass

rps = ["scissor", "paper", "rock"]

# get player input
try:
    print("ROCK PAPER SCISSOR GAME")
    player_input = input("ENTER rock, paper, or scissors: ")
    player_val = player_input.lower().strip()
    if player_val not in rps:
        raise InvalidRPSError
except InvalidRPSError:
    print("Please type rock, paper, scissor next time")
    sys.exit(0) # exit gracefully
except:
    print("Something terrible happened")

# get npc input
npc_num = random.randrange(3)
npc_val = rps[npc_num]

# debug msgs
# player_val = "rock"
# npc_val = "paper"
# print(f"PLAYER = {player_val}")
# print(f"NPC = {npc_val}")


tie_msg = "Tie game!"
lose_msg = "Sorry :( You lost this one"
win_msg = "Congratulations! You won"

# TIE MSG
if player_val == npc_val:
    print(tie_msg)
# ROCK CONDITIONS
elif npc_val == "rock":
    if player_val == "scissor":
        print(lose_msg)
    else:
        print(win_msg)
# PAPER CONDITIONS
elif npc_val == "paper":
    if player_val == "rock":
        print(lose_msg)
    else:
        print(win_msg)
# SCISSOR CONDITIONS
else:
    if player_val == "paper":
        print(lose_msg)
    else:
        print(win_msg)
