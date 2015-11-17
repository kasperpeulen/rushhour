from rushhour.position import Position

test1 = Position.new(1, 1) + Position.new(2, 2) == Position.new(3, 3)
print("Positions can be added " + str(test1))
