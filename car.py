class Car:
    '''todo'''
    boardLength = 6

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

    def __str__(self):
        s = "\n"
        for y in range(0, self.boardLength):
            for x in range(0, self.boardLength):
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

    def __str__(self):
        return "Position(" + str(self.x) + ", " + str(self.y) + ")"


car1 = Car(Position(0, 0), True, 2)
car2 = Car(Position(0, 0), False, 2)
car3 = Car(Position(0, 0), True, 3)
car4 = Car(Position(0, 0), False, 3)


test1 = Position(1, 1) + Position(2, 2) == Position(3, 3)
print "Positions can be added " + str(test1)

test2 = car1.end == Position(1, 0)
print "End position is correct for horizontal " + str(test2)

test3 = car2.end == Position(0, 1)
print "End position is correct for vertical " + str(test3)

test4 = car3.positions == [Position(0, 0), Position(1, 0), Position(2, 0)]
print "Positions are correct for horizontal " + str(test4)

print(car1)

list = [True, False, False]
