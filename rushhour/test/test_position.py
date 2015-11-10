from rushhour.position import Position

test1 = Position(1, 1) + Position(2, 2) == Position(3, 3)
print("Positions can be added " + str(test1))
