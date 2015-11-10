import os
import random

from rushhour.car import Car
from rushhour.hash_table import states_checked_hash_table
from rushhour.position import Position
from typing import List
from termcolor import colored, COLORS, HIGHLIGHTS, ATTRIBUTES, RESET


class Board:
    """ todo """

    def __init__(self, board_width: int, board_height: int, cars: List[Car],
                 goal: Position, previous=None):
        Car.boardHeight = board_height
        Car.boardWidth = board_width
        self.previous = previous
        self.cars = cars
        self.goal = goal

    def is_winner(self) -> bool:
        return self.cars[0].end == self.goal

    def possible_next_boards(self):
        new_boards = []
        for i in range(0, len(self.cars)):
            for new_car in self.cars[i].next_cars(other_cars=list(self.cars)):
                new_cars = list(self.cars)
                new_cars[i] = new_car
                board = Board(Car.boardHeight, Car.boardWidth, new_cars,
                              self.goal, previous=self)

                if board.is_winner():
                    print("yeaaaaah")
                    state = board
                    winning_path = []
                    while state != None:
                        winning_path.append(state)
                        state = state.previous
                    winning_path.reverse()
                    for board in winning_path:
                        print(board)
                    exit(0)

                hash0 = hash(board)
                if hash0 not in states_checked_hash_table:
                    states_checked_hash_table[hash0] = [board]
                    new_boards.append(board)

                if hash0 in states_checked_hash_table and board not in \
                        states_checked_hash_table[hash0]:
                    new_boards.append(board)
                    states_checked_hash_table[hash0].append(board)

        return new_boards

    def car_that_contains_position(self, position: Position):
        for i in range(0, len(self.cars)):
            if position in self.cars[i].positions:
                return self.cars[i]
        return None

    def __str__(self, *args, **kwargs):
        board = '\n'
        for y in range(0, Car.boardHeight):
            for x in range(0, Car.boardWidth):
                if self.car_that_contains_position(Position(x, y)) is not None:
                    i = self.cars.index(
                        self.car_that_contains_position(Position(x, y)))
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
        return str(other) == str(self)


def color(text, i):
    """Colorize text.

    Available text colors:
        red, green, yellow, blue, magenta, cyan, white.

    Available text highlights:
        on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed.

    Example:
        colored('Hello, World!', 'red', 'on_grey', ['blue', 'blink'])
        colored('Hello, World!', 'green')
    """
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        fmt_str = '\033[%dm%s'
        text = fmt_str % (i % 7 + 30, text)
        COLORS
        text += RESET
    return text