import os
import random

import time

from rushhour.car import Car
from rushhour.hash_table import states_checked_hash_table
from rushhour.position import Position
from typing import List
from termcolor import colored, COLORS, HIGHLIGHTS, ATTRIBUTES, RESET

from rushhour.range import Goal


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
        (index, pos) = goal
        self.goal = Goal.from_position(index, pos)

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
                    raise Win

                hash0 = hash(board)
                if hash0 not in states_checked_hash_table:
                    states_checked_hash_table[hash0] = [board]
                    new_boards.append(board)
                elif board not in \
                        states_checked_hash_table[hash0]:
                    new_boards.append(board)
                    states_checked_hash_table[hash0].append(board)

        return new_boards

    def cars_that_clash_with_goal(self) -> List[Car]:
        (goal_index, goal_position) = self.goal
        red_car = self.cars[goal_index]
        other_cars = List(self.cars)
        other_cars.remove(red_car)
        move_car = red_car.move(1)

        while(move_car.end != goal_position):

            red_car.move(1).no_clash_all_cars(other_cars)
            red_car

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