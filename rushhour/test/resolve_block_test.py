from rushhour.board import MegaCar


from rushhour.games import game2, game3
from rushhour.position import Position

board = game3

print(board)

# board.goal = (0, Position.new(5, 3))
# print(board.blocking_cars()[1])

resolve_block = (board.cars[6].resolve_block(MegaCar.from_board(board)))

possible_moves = (board.cars[6].possible_movement(board.cars))

print(set.intersection(set(resolve_block), set(possible_moves)))