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



    # def possible_next_boards(self):
    #     new_boards = []
    #     for car in self.cars:
    #         for new_car in car.next_cars():
    #

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
                    i = self.cars.index(self.car_that_contains_position(Position(x, y)))
                    board += str(i).zfill(2) + ' '
                else:
                   board += 'XX '
            board += '\n'
        return board
