"""
This contains the player entity
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


import math
import textwrap

from die import Die


class Player:
    """
    Player entity that will be used to interact with the
    game board
    """

    def __init__(self, name: str, is_bot: bool):
        if not (isinstance(name, str) and isinstance(is_bot, bool)):
            raise ValueError(
                f'mismatched type for Player constructor: Player({type(name)}, {type(is_bot)})'
            )
        self.name = name
        self.is_bot = is_bot
        self.die = Die(7 if self.is_bot else 6)
        self.current_roll = math.inf
        self.current_score = 0

    def roll(self) -> None:
        """
        Roll the dice currently held by the player
        """

        self.current_roll = self.die.roll()

    def print_die(self):
        """
        Print dice rolled to the screen
        """

        content = f"""
                [INFO]: {self.name}'{'' if(self.name[-1].lower() == 's') else 's'} roll
                #########
                #       #
                #   {self.current_roll}   #
                #       #
                #########
                """
        print(textwrap.dedent(content).strip())
