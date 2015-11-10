from rushhour.car import Car
from rushhour.position import Position
from typing import List


class Board:
    """ todo """

    def __init__(self, board_width: int, board_height: int, cars: List[Car], goal: Position):
        Car.boardHeight = board_height
        Car.boardWidth = board_width
        self.cars = cars
        self.goal = goal

    def is_winner(self) -> bool:
        return self.cars[0].end == self.goal
