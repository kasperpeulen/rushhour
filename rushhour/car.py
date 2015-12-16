from .position import Position
from typing import List, Set

class Car:
    """
    Class for cars specified by start, horizontal and length
    """
    boardWidth = 6
    boardHeight = 6

    @staticmethod
    def new(start: Position, horizontal: bool, length: int, immobile=False):
        """
        Check if position is already in cache. If not make new instance and save in cache.
        """
        hash = start.x + start.y * 100
        if horizontal:
            hash += 10000
        if length == 3:
            hash += 100000
        if hash in cache:
            return cache[hash]
        else:
            new_car = Car(start, horizontal, length, hash, immobile)
            cache[hash] = new_car
            return new_car

    def __init__(self, start: Position, horizontal: bool, length: int, hash,
                 immobile=False):
        """
        Make position consisting of starting position (x,y), horizontal boolean (if horizontal: True, if vertical:
        False) and the length of the car (2 or 3).
        """
        self.hash = hash
        self.start = start
        self.horizontal = horizontal
        self.length = length
        self.immobile = immobile

        # calculate end position 
        if self.horizontal and length == 2:
            self.end = self.start + Position.new(1, 0)
            self.positions = [self.start, self.end]
        elif not self.horizontal and length == 2:
            self.end = self.start + Position.new(0, 1)
            self.positions = [self.start, self.end]
        elif self.horizontal and length == 3:
            self.end = self.start + Position.new(2, 0)
            self.positions = [self.start, self.start + Position.new(1, 0),
                              self.end]
        else:
            self.end = self.start + Position.new(0, 2)
            self.positions = [self.start, self.start + Position.new(0, 1),
                              self.end]

    def is_valid(self) -> bool:
        """
        Check if new position is still on the board.
        """
        return self.start.x >= 0 \
               and self.start.y >= 0 \
               and self.end.x < self.boardWidth \
               and self.end.y < self.boardHeight

    def move(self, steps: int) -> 'Car':
        """
        Move car "step" amount of places.
        """
        if self.horizontal:
            return Car.new(self.start + Position.new(steps, 0), self.horizontal,
                           self.length)
        else:
            return Car.new(self.start + Position.new(0, steps), self.horizontal,
                           self.length)

    def no_clash_all_cars(self, other_cars: List['Car']):
        """
        Check if new car clashes with other cars (list).
        """
        for other_car in other_cars:
            if not self.no_clash(other_car):
                return False
        return True

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

    def next_cars(self, other_cars: List['Car']) -> List['Car']:
        """
        Check all possible new positions of car
        """

        if self.immobile:
            return []

        # make sure self is removed if it is in the list of other cars
        if self in other_cars:
            other_cars.remove(self)
        new_cars = []
        new_car = self.move(1)
        while new_car.is_valid() and new_car.no_clash_all_cars(other_cars):
            new_cars.append(new_car)
            new_car = new_car.move(1)

        new_car = self.move(-1)
        while new_car.is_valid() and new_car.no_clash_all_cars(other_cars):
            new_cars.append(new_car)
            new_car = new_car.move(-1)

        return new_cars

    def goal_pos_from_move(self, move: int) -> Position:
        if self.horizontal:
            if move > 0:
                goal_pos = Position.new(self.end.x + move, self.end.y)
            else:
                goal_pos = Position.new(self.start.x + move, self.start.y)
        else:
            if move > 0:
                goal_pos = Position.new(self.end.x, self.end.y + move)
            else:
                goal_pos = Position.new(self.start.x, self.start.y + move)
        return goal_pos

    def real_possible_moves(self, other_cars: List['Car'], goal) -> Set:
        possible_movement = self.possible_movement(other_cars)
        from rushhour.board import MegaCar
        resolve_block_list = self.resolve_block(MegaCar.from_goal(goal, other_cars))
        return set.intersection(set(possible_movement), set(resolve_block_list))

    def possible_movement(self, other_cars: List['Car']) -> List[int]:
        cars_in_line = self.cars_in_line(other_cars)

        cars_in_line_negative = 0
        for car in cars_in_line:
            if self.horizontal:
                if car.end.x < self.start.x:
                    cars_in_line_negative += car.length
            else:
                if car.end.y < self.start.y:
                    cars_in_line_negative += car.length

        # print(cars_in_line_negative)

        cars_in_line_positive = 0
        for car in cars_in_line:
            if self.horizontal:
                if car.start.x > self.end.x:
                    cars_in_line_positive += car.length
            else:
                if car.start.y > self.end.y:
                    cars_in_line_positive += car.length
        # print(cars_in_line_positive)

        moves = []
        if self.horizontal:
            can_move_negative = self.start.x - cars_in_line_negative
        else:
            can_move_negative = self.start.y - cars_in_line_negative

        if self.horizontal:
            can_move_positive = Car.boardWidth - self.end.x - cars_in_line_positive - 1
        else:
            can_move_positive = Car.boardHeight - self.end.y - cars_in_line_positive - 1

        for i in range(-1, -can_move_negative - 1, -1):
            moves.append(i)
        for i in range(1, can_move_positive + 1, 1):
            moves.append(i)
        return moves

    def resolve_block(self, mega_car: 'MegaCar') -> List[int]:
        moves = []

        if not self.horizontal:
            negative_move = self.end.y - mega_car.start.y + 1
        else:
            negative_move = self.end.x - mega_car.start.x + 1

        if not self.horizontal:
            positive_move = self.start.y - mega_car.start.y - 1
        else:
            positive_move = self.start.x - mega_car.start.x - 1

        negative_move = -negative_move
        positive_move = -positive_move

        while True:
            moves.append(negative_move)
            if self.horizontal:
                if self.start.x + negative_move <= 0:
                    break
            else:
                if self.start.y + negative_move <= 0:
                    break
            negative_move += -1

        while True:
            moves.append(positive_move)
            if self.horizontal:
                if self.end.x + positive_move >= Car.boardWidth - 1:
                    break
            else:
                if self.end.y + positive_move >= Car.boardHeight - 1:
                    break
            positive_move += 1
        return moves

    def cars_in_line(self, other_cars: List['Car']) -> List['Car']:
        other_cars = list(other_cars)
        other_cars.remove(self)
        result = []
        for car in other_cars:
            if car.horizontal:
                if self.horizontal and car.start.y == self.start.y:
                    result.append(car)
            else:
                if not self.horizontal and car.start.x == self.start.x:
                    result.append(car)
        return result

    def __str__(self) -> str:
        """
        Visualize the car in the board. C means there is a car at that position, X means there is no car
        """
        s = "\n"
        for y in range(0, self.boardHeight):
            for x in range(0, self.boardWidth):
                if Position.new(x, y) in self.positions:
                    s += "C "
                else:
                    s += "X "
            s += "\n"
        return s

    def __hash__(self) -> int:
        return self.hash


cache = {}
