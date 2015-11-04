class Car:
    '''todo'''
    boardWidth = 6
    boardHeight = 6

    def __init__(self, start, horizontal, length):
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

    def move(self, steps):
        if self.horizontal:
            return Car(self.start + Position(steps, 0), self.horizontal, self.length)
        else:
            return Car(self.start + Position(0, steps), self.horizontal, self.length)

    def no_clash(self, othercar):
        set1 = set(self.positions)
        set2 = set(othercar.positions)
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


class Position:
    '''todo'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __radd__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return "Position(" + str(self.x) + ", " + str(self.y) + ")"


class Board:
    ''' todo '''

    def __init__(self, boardWidth, boardHeight, cars, goal):
        Car.boardHeight = boardHeight
        Car.boardWidth = boardWidth
        self.cars = cars
        self.goal = goal

    def is_Winner(self):
        return self.cars[0].end == self.goal

##board tests


# tests
car1 = Car(Position(0, 0), True, 2)
car2 = Car(Position(0, 0), False, 2)
car3 = Car(Position(0, 0), True, 3)
car4 = Car(Position(0, 0), False, 3)

Car.boardWidth = 6
Car.boardHeight = 6

test1 = Position(1, 1) + Position(2, 2) == Position(3, 3)
print "Positions can be added " + str(test1)

test2 = car1.end == Position(1, 0)
print "End position is correct for horizontal " + str(test2)

test3 = car2.end == Position(0, 1)
print "End position is correct for vertical " + str(test3)

test4 = car3.positions == [Position(0, 0), Position(1, 0), Position(2, 0)]
print "Positions are correct for horizontal " + str(test4)

test5 = car1.is_valid() == True
print "car position can be valid " + str(test5)

car_invalid = Car(Position(5, 5), True, 2)

test6 = car1.is_valid() == False
print "car position can be invalid " + str(test5)

car_moved = car1.move(3)
test7 = car_moved.start == Position(3, 0)
test8 = car_moved.is_valid()

print "car can be moved " + str(test7)
print "car moved can be valid " + str(test8)

car_moved_invalid = car1.move(-3)

test9 = car_moved_invalid.is_valid() == False

print "car moved can be invalid " + str(test9)

new_cars = car1.next_cars()

print "new cars are computed " + str(len(new_cars) == 4)

car5 = Car(Position(4, 4), True, 2)

new_cars_backwards = car5.next_cars()

print "new cars can be placed backwards " + str(len(new_cars_backwards) == 4)

test10 = car1.no_clash(car2) == False

print "car can clash " + str(test10)

car6 = Car(Position(2, 0), True, 2)

test11 = car1.no_clash(car6) == True

print "car cannot clash " + str(test11)

board = Board(6, 6, [Car(Position(0, 0), True, 2),], Position(5, 2))
test12 = board.is_Winner() == False

print "board can be no winner " + str(test12)
