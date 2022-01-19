#!/usr/bin/env python3.9

"""
Driver code for the pig game
"""

# Jared Dyreson
# CPSC 386-01
# 2021-10-02
# jareddyreson@csu.fullerton.edu
# @JaredDyreson
#
# Lab 00-02
#
# Some filler text
#

from player import Player
from pig_game import PigGame

PLAYERS = []

is_single_player = input(
    "[INPUT] Is this a single player game? [y/n]: ").lower()
if(bot_flag := (is_single_player in ('y', 'yes'))):
    PLAYER_COUNT = 1
else:
    PLAYER_COUNT = int(input("[INPUT] Player count: "))

for x in range(0, PLAYER_COUNT):
    name = input(f'Player {x}\'s name: ')
    PLAYERS.append(Player(name, False))

if bot_flag:
    PLAYERS.append(Player("BOT", True))

GAME_INSTANCE = PigGame(
    players=PLAYERS, is_single_player=bot_flag, max_score=10)

# umm okay PEP8, chill out with the UPPERCASE constant thing
GAME_INSTANCE.game_loop()
