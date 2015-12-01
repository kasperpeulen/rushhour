from rushhour.position import Position
from typing import List


class Range:
    def __init__(self, begin: int, end: int):
        self.begin = begin
        self.end = end

    def get_list(self) -> List[int]:
        return list(range(self.begin, self.end + 1))

class Goal:
    def __init__(self, car: 'Car', moves: int):
        self.car = car
        self.moves = moves
        self.end_position = car.move(moves).end

    @staticmethod
    def from_position(car: 'Car', goal_pos: Position):
        if car.horizontal:
            beginx = car.end.x
            endx = goal_pos.x
            moves = endx - beginx
        else:
            beginy = car.end.y
            endy = goal_pos.y
            moves = endy - beginy
        return Goal(car, moves)

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
        print(self.x.get_list())
        print(self.y.get_list())

        for y in range(0, Car.boardHeight):
            for x in range(0, Car.boardWidth):
                if x in self.x.get_list() and y in self.y.get_list():
                    s += "C "
                else:
                    s += "X "
            s += "\n"
        return s

class Car:
    """
    Class for cars specified by start, horizontal and length
    """
    boardWidth = None
    boardHeight = None

    @staticmethod
    def new(start: Position, horizontal: bool, length: int, immobile=False):
        """
        Check if position is already in cache. If not make new instance and save in cache.
        """
        hash = start.x + start.y * 100
        if horizontal:
            hash += 1000
        if length == 3:
            hash += 10000
        if hash in cache:
            return cache[hash]
        else:
            new_car = Car(start, horizontal, length, hash, immobile)
            cache[hash] = new_car
            return new_car

    def __init__(self, start: Position, horizontal: bool, length: int, hash, immobile=False):
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
            self.positions = [self.start, self.start + Position.new(1, 0), self.end]
        else:
            self.end = self.start + Position.new(0, 2)
            self.positions = [self.start, self.start + Position.new(0, 1), self.end]

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


    def clashes_with_range(self, range: PositionRange):
        """
        Check if car clashes with imaginary car that can be of any length.
        """
        return (self.end.x >= range.x.begin and
                self.start.x <= range.x.end and
                self.end.y >= range.y.begin and
                self.start.y <= range.y.end)


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
