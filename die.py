"""
This contains the dice entity
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

import random


class Die:
    """
    Die entity that will be used to influence the game state
    """

    def __init__(self, sides: int):
        if not isinstance(sides, int):
            raise ValueError(
                f'expected sides to be of type `int`, received: {type(int)}'
            )
        self.sides = sides

    def roll(self) -> int:
        """
        Roll the dice:
        invokes the random number generator to replicate this in real life
        """

        return random.randint(0, self.sides)

    def so_you_can_shut_it(self):
        """
        really PEP8?
        this is stupid
        """
        return 0
