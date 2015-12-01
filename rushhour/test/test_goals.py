from rushhour.games import game7
from rushhour.car import PositionRange, Goal, Car

game = game7

Car.boardWidth = game7.board_width
Car.boardHeight = game7.board_height

print(PositionRange.from_goal(game7.temp_goal))
