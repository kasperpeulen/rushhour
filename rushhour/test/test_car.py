from rushhour.car import Car
from rushhour.position import Position

car1 = Car(length=2, start=Position.new(0, 0), horizontal=True)
car2 = Car(Position.new(0, 0), False, 2)
car3 = Car(Position.new(0, 0), True, 3)
car4 = Car(Position.new(0, 0), False, 3)

Car.boardWidth = 6
Car.boardHeight = 6

test2 = car1.end == Position.new(1, 0)
print("End position is correct for horizontal " + str(test2))

test3 = car2.end == Position.new(0, 1)
print("End position is correct for vertical " + str(test3))

test4 = car3.positions == [Position.new(0, 0), Position.new(1, 0), Position.new(2, 0)]
print("Positions are correct for horizontal " + str(test4))

test5 = car1.is_valid() == True
print("car position can be valid " + str(test5))

car_invalid = Car(Position.new(5, 5), True, 2)

test6 = car1.is_valid() == False
print("car position can be invalid " + str(test5))

car_moved = car1.move(3)
test7 = car_moved.start == Position.new(3, 0)
test8 = car_moved.is_valid()

print("car can be moved " + str(test7))
print("car moved can be valid " + str(test8))

car_moved_invalid = car1.move(-3)

test9 = car_moved_invalid.is_valid() == False

print("car moved can be invalid " + str(test9))

car5 = Car(Position.new(4, 4), True, 2)

test10 = car1.no_clash(car2) == False

print("car can clash " + str(test10))

car6 = Car(Position.new(2, 0), True, 2)

test11 = car1.no_clash(car6) == True

print("car cannot clash " + str(test11))

car10 = Car(Position.new(0, 0), True, 2)
car11 = Car(Position.new(2, 0), True, 2)
car12 = Car(Position.new(4, 0), True, 2)
car13 = Car(Position.new(0, 1), True, 2)

test12 = car13.next_cars([car13, car10, car11, car12])

print("car can move freely", str(len(test12) == 4))

car14 = Car(Position.new(2, 1), True, 2)

test13 = car13.next_cars([car13, car10, car11, car12, car14])

print("car can not hop", str(len(test13) == 0))

print("car can be equal " + str(
    Car(Position.new(0, 0), True, 2) == Car(Position.new(0, 0), True, 2)))
