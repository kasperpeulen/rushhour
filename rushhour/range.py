from typing import List

from rushhour.car import Car
from rushhour.position import Position


class PositionRange:
    def __init__(self, x: Range, y: Range):
        self.x = x
        self.y = y

    @staticmethod
    def from_goal(goal: Goal):
        if goal.car.horizontal:
            y = Range(goal.car.start.y, goal.car.start.y)
            x = Range(goal.car.end.x + 1, goal.car.end.x + goal.moves)
        else:
            y = Range(goal.car.end.y + 1, goal.car.end.y + goal.moves)
            x = Range(goal.car.end.x, goal.car.end.x)
        return PositionRange(x, y)

    def __str__(self) -> str:
        """
        Visualize the car in the board. C means there is a car at that position, X means there is no car
        """
        s = "\n"
        for y in range(0, Car.boardHeight):
            for x in range(0, Car.boardWidth):
                if x in self.x.get_list() and y in self.y.get_list():
                    s += "C "
                else:
                    s += "X "
            s += "\n"
        return s

class Range:
    def __init__(self, begin: int, end: int):
        self.begin = begin
        self.end = end

    def get_list(self) -> List[int]:
        return range(self.begin, self.end)

class Goal:
    def __init__(self, car: Car, moves: int):
        self.car = car
        self.moves = moves
        self.end_position = car.move(moves).end

    @staticmethod
    def from_position(car: Car, goal_pos: Position):
        if car.horizontal:
            beginx = car.end.x
            endx = goal_pos.x
            moves = endx - beginx
        else:
            beginy = car.end.y
            endy = goal_pos.y
            moves = endy - beginy
        return Goal(car, moves)
