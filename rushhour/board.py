import os
import random

import time

from rushhour import hash_table
from rushhour.car import Car
from rushhour.position import Position
from typing import List
from termcolor import colored, COLORS, HIGHLIGHTS, ATTRIBUTES, RESET


class Board:
    """
    Board definition
    """

    def __init__(self, board_width: int, board_height: int, cars: List[Car],
                 goal: (int, Position), previous=None):
        """
        Define values for board. Previous is parental state for path checking.
        """
        self.board_height = board_height
        self.board_width = board_width
        self.previous = previous
        self.cars = cars
        self.goal = goal
        # (index, pos) = goal
        # self.temp_goal = Goal.from_position(cars[index], pos)
        self.moves = ""

    def is_winner(self) -> bool:
        """
        Check if car is at goal (board exit).
        """
        (index, position) = self.goal
        return self.cars[index].end == position

    def possible_next_boards(self):
        """
        Define new possible boards (states).
        """
        new_boards = []
        for i in range(0, len(self.cars)):
            for new_car in self.cars[i].next_cars(other_cars=list(self.cars)):
                new_cars = list(self.cars)
                new_cars[i] = new_car
                board = Board(self.board_height, self.board_width, new_cars,
                              self.goal, previous=self)
                board.moves = str(i)

                if board.is_winner():
                    print("yeaaaaah")
                    state = board
                    winning_path = []
                    while state is not None:
                        winning_path.append(state)
                        state = state.previous
                    winning_path.reverse()
                    for board in winning_path:
                        print(board)
                        print(board.moves)
                    raise Win(board)

                hash0 = hash(board)
                if hash0 not in hash_table.states_checked_hash_table:
                    hash_table.states_checked_hash_table[hash0] = [board]
                    new_boards.append(board)
                elif board not in \
                        hash_table.states_checked_hash_table[hash0]:
                    new_boards.append(board)
                    hash_table.states_checked_hash_table[hash0].append(board)

        return new_boards

    def car_that_contains_position(self, position: Position):
        """
        Returns car at certain position.
        """
        for i in range(0, len(self.cars)):
            if position in self.cars[i].positions:
                return self.cars[i]
        return None

    def __str__(self, *args, **kwargs):
        """
        Give color and number to cars in visualization.
        """
        board = '\n'
        for y in range(0, self.board_height):
            for x in range(0, self.board_width):
                if self.car_that_contains_position(Position.new(x, y)) is not None:
                    i = self.cars.index(
                        self.car_that_contains_position(Position.new(x, y)))
                    if i == 0:

                        board += colored(str(i).zfill(2), 'red') + ' '
                    else:
                        board += color(str(i).zfill(2), i) + ' '

                else:
                    board += 'XX '
            board += '\n'
        return board

    def __hash__(self) -> int:
        return hash(tuple(self.cars))

    def __eq__(self, other: 'Board') -> bool:
        return self.cars == other.cars


def color(text, i):
    """Colorize text.

    Available text colors:
        red, green, yellow, blue, magenta, cyan, white.
    """
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        fmt_str = '\033[%dm%s'
        text = fmt_str % (i % 7 + 30, text)
        text += RESET
    return text

class Win(Exception):
    """
    Raised when solution is found.
    """
    def __init__(self, board: Board):
        self.board = board
