from rushhour.board import Board
from rushhour.car import Car
from rushhour.games import game2
from rushhour.position import Position

board1 = Board(6, 6, [Car(Position(0, 0), True, 2)], Position(5, 2))
test12 = board1.is_winner() == False

print("board can be no winner " + str(test12))

board2 = Board(6, 6, [Car(Position(0, 0), True, 2)], Position(5, 2))
board3 = Board(6, 6, [Car(Position(0, 1), True, 2), Car(Position(2,2), True, 3)], Position(5, 2))

stage2 = game2.possible_next_boards()
for board in stage2:
    print(board)