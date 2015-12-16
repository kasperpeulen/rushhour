from rushhour.board import Board
from rushhour.car import Car
from rushhour.position import Position

board = Board(cars=[
    Car.new(Position.new(2, 2), True, 2),
    Car.new(Position.new(0, 4), True, 2),
    Car.new(Position.new(4, 0), False, 3),
    Car.new(Position.new(4, 4), True, 2)
], goal=(0, Position.new(5, 2)),
    board_height=6,
    board_width=6
)

Car.boardWidth = board.board_width
Car.boardHeight = board.board_height
print(board)

my_car = board.cars[3]

in_line_cars = my_car.cars_in_line(board.cars)

print(in_line_cars[0])
print(my_car.possible_movement(board.cars))

print(board.blocking_cars()[0].possible_movement(board.cars))