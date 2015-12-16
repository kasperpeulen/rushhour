from rushhour.car import Car
from rushhour.games import game2, game3, game4, game1, game5, game6, game7

board = game3

Car.boardWidth = 6
Car.boardHeight = 6

print(board)

print(board.a_star_count())