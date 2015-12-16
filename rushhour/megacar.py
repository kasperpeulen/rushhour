from .car import *
from .board import *
from typing import List

class MegaCar:
    def __init__(self, start, end):
        self.start = start
        self.end = end

        if start.y == end.y:
            self.horizontal = True
            self.length = end.x - start.x
        else:
            self.horizontal = False
            self.length = end.y - end.x

        if self.length == 2
            self.positions = [start, end]
        else:
            if self.horizontal:
                self.positions = [start, start + Position.new(1, 0), end]
            else:
                self.positions = [start, start + Position.new(0, 1), end]

    def no_clash(self, other_car: 'Car') -> bool:
        """
        Check if car clashes with specific car.
        """
        other_start = other_car.start
        other_end = other_car.end

        return not (self.end.x >= other_start.x and
                    self.start.x <= other_end.x and
                    self.end.y >= other_start.y and
                    self.start.y <= other_end.y)

    def no_clash_all_cars(self, other_cars: List['Car']) -> List['Car']:
        """
        Check if new car clashes with other cars (list).
        """
        result = []
        for other_car in other_cars:
            if not self.no_clash(other_car):
                result.append(other_car)
        return result

    def move(self, steps: int) -> 'MegaCar':
        """
        Move car "step" amount of places.
        """
        if self.horizontal:
            return Car.new(self.start + Position.new(steps, 0), self.horizontal,
                           self.length)
        else:
            return Car.new(self.start + Position.new(0, steps), self.horizontal,
                           self.length)

    @staticmethod
    def from_board(board):
        (index, pos) = board.goal
        mega_car = MegaCar(
            Position.new(board.cars[index].end.x + 1, board.cars[index].end.y),
            pos
        )
        return mega_car

