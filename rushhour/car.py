from rushhour.position import Position
from typing import List


class Car:
    """ todo """
    boardWidth = 6
    boardHeight = 6

    @staticmethod
    def new(start: Position, horizontal: bool, length: int):
        hash = start.x + start.y * 100

        car = Car(start, horizontal, length)

        if hash in cache:
            if car in cache[hash]:
                return car
            else:
                cache[hash].append(car)
                return car
        else:
            cache[hash] = [car]
            return car

    def __init__(self, start: Position, horizontal: bool, length: int):
        self.start = start
        self.horizontal = horizontal
        self.length = length

        if self.horizontal:
            self.end = self.start + Position.new(length - 1, 0)
        else:
            self.end = self.start + Position.new(0, length - 1)

        if length == 2:
            self.positions = [self.start, self.end]
        else:
            if horizontal:
                self.positions = [self.start, self.start + Position.new(1, 0),
                                  self.end]
            else:
                self.positions = [self.start, self.start + Position.new(0, 1),
                                  self.end]

    def is_valid(self) -> bool:
        return self.start.x >= 0 \
               and self.start.y >= 0 \
               and self.end.x < self.boardWidth \
               and self.end.y < self.boardHeight

    def move(self, steps: int) -> 'Car':
        if self.horizontal:
            return Car.new(self.start + Position.new(steps, 0), self.horizontal,
                       self.length)
        else:
            return Car.new(self.start + Position.new(0, steps), self.horizontal,
                       self.length)

    def no_clash_all_cars(self, other_cars: List['Car']):
        for other_car in other_cars:
            if not self.no_clash(other_car):
                return False
        return True

    def no_clash(self, other_car: 'Car') -> bool:
        set1 = set(self.positions)
        set2 = set(other_car.positions)
        if set1.intersection(set2) == set([]):
            return True
        else:
            return False

    def next_cars(self, other_cars: List['Car']) -> List['Car']:
        """
        Calculates all possible next cars bounded by the [boardWidth] and
        [boardHeight]. Doesn't remove cars that overlap.
        """
        # make sure self is removed if it is in the list of other cars
        if self in other_cars:
            other_cars.remove(self)
        new_cars = []
        new_car = self.move(1)
        while new_car.is_valid():
            if new_car.no_clash_all_cars(other_cars):
                new_cars.append(new_car)
            else:
                break
            new_car = new_car.move(1)

        new_car = self.move(-1)
        while new_car.is_valid():
            if new_car.no_clash_all_cars(other_cars):
                new_cars.append(new_car)
            else:
                break
            new_car = new_car.move(-1)

        return new_cars

    def __str__(self) -> str:
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
        return hash((self.start, self.horizontal, self.length))

    def __eq__(self, other: 'Car') -> bool:
        return self.positions == other.positions

cache = {}