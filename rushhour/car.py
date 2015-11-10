from rushhour.position import Position


class Car:
    """ todo """
    boardWidth = 6
    boardHeight = 6

    def __init__(self, start: Position, horizontal: bool, length: int):
        self.start = start
        self.horizontal = horizontal
        self.length = length

        if self.horizontal:
            self.end = self.start + Position(length - 1, 0)
        else:
            self.end = self.start + Position(0, length - 1)

        if length == 2:
            self.positions = [self.start, self.end]
        else:
            if horizontal:
                self.positions = [self.start, self.start + Position(1, 0), self.end]
            else:
                self.positions = [self.start, self.start + Position(0, 1), self.end]

    def is_valid(self):
        return self.start.x >= 0 \
               and self.start.y >= 0 \
               and self.end.x < self.boardWidth \
               and self.end.y < self.boardHeight

    def move(self, steps: int):
        if self.horizontal:
            return Car(self.start + Position(steps, 0), self.horizontal, self.length)
        else:
            return Car(self.start + Position(0, steps), self.horizontal, self.length)

    def no_clash(self, other_car: 'Car'):
        set1 = set(self.positions)
        set2 = set(other_car.positions)
        if set1.intersection(set2) == set([]):
            return True
        else:
            return False

    def next_cars(self):
        new_cars = []

        new_car = self.move(1)
        while new_car.is_valid():
            new_cars.append(new_car)
            new_car = new_car.move(1)

        new_car = self.move(-1)
        while new_car.is_valid():
            new_cars.append(new_car)
            new_car = new_car.move(-1)

        return new_cars

    def __str__(self):
        s = "\n"
        for y in range(0, self.boardHeight):
            for x in range(0, self.boardWidth):
                if Position(x, y) in self.positions:
                    s += "C "
                else:
                    s += "X "
            s += "\n"
        return s

