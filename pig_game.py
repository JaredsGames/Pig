"""
This contains the PigGame class
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
import typing
import random
import re

from player import Player


class PigGame:
    """
    Pig implementation
    """

    def __init__(self, players, is_single_player: bool, max_score=100):
        if not (
            isinstance(is_single_player, bool)
            and isinstance(players, list)
            and all(isinstance(_, Player) for _ in players)
            and isinstance(max_score, int)
        ):
            raise ValueError

        self.is_single_player = is_single_player
        self.players = players

        for player in self.players:
            player.roll()

        self.players = sorted(self.players, key=lambda x: x.current_roll)
        self.count = len(self.players)
        self.max_score = max_score

    def get_input(self) -> bool:
        """
        Ensure user is giving the correct input
        """

        _exit = False
        while not _exit:
            user_input = input("[INPUT]: Hold (y/n): ")
            if re.match("^y(es)?", user_input, re.IGNORECASE):
                return True
            if re.match("^n(o)?", user_input, re.IGNORECASE):
                return False

    def find_winner(self, comparator: typing.Callable):  # tuple[int, int]
        """
        Search through the player base to find a winner
        based on a criteria given.
        This can extend or diminish the game's lifespan
        """

        for index, element in enumerate(self.players):
            if comparator(element):
                return (True, index)
        return (False, math.inf)

    def game_loop(self):
        """
        Main game instance
        """

        exit_condition = False

        i, index = 0, 0

        print(f'[INFO] Game is starting with: {self.players[i].name}')

        while not exit_condition:  # outer game loop
            hold = False
            accrued_points = 0
            lost_everything = False

            # current player loop
            while not hold:
                self.players[i].roll()
                self.players[i].print_die()
                if self.players[i].current_roll == 1:
                    lost_everything = True
                    break
                accrued_points += self.players[i].current_roll
                if self.is_single_player and self.players[i].is_bot:
                    hold = random.random() <= 0.2
                else:
                    # input_value = input("[INPUT]: Hold (y/n): ")
                    # hold = True
                    hold = self.get_input()
                # hold = True
                # hold = random.random() <= 0.5 # emulates human element (use
                # input)
                if hold:
                    self.players[i].current_score += accrued_points
                    print(f'[INFO] {self.players[i].name} will hold')
                    break
            if lost_everything:
                print(
                    f'[INFO] {self.players[i].name} rolled a 1, you have lost your turn!'
                )

            exit_condition, index = self.find_winner(
                lambda x: x.current_score >= self.max_score
            )

            i = 0 if (i == self.count - 1) else i + 1
            print()

        print(
            f'[INFO] Game winner is {self.players[index].name}  \
                with {self.players[index].current_score} point(s)!')
