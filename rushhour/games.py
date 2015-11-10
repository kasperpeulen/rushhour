from rushhour.board import Board
from rushhour.car import Car
from rushhour.position import Position

game2 = Board(cars=[
    Car(length=2, horizontal=True, start=Position(2, 2)),
    Car(length=2, horizontal=True, start=Position(2, 0)),
    Car(length=2, horizontal=True, start=Position(4, 0)),
    Car(length=2, horizontal=True, start=Position(1, 1)),
    Car(length=2, horizontal=True, start=Position(3, 1)),
    Car(length=3, horizontal=False, start=Position(5, 1)),
    Car(length=2, horizontal=False, start=Position(4, 2)),
    Car(length=2, horizontal=True, start=Position(0, 3)),
    Car(length=2, horizontal=True, start=Position(2, 3)),
    Car(length=2, horizontal=False, start=Position(0, 4)),
    Car(length=2, horizontal=False, start=Position(3, 4)),
    Car(length=2, horizontal=True, start=Position(4, 4)),
    Car(length=2, horizontal=True, start=Position(4, 5)),
], goal=Position(5, 2),
    board_height=6,
    board_width=6
)

level1 = Board(cars=[
    Car(Position(2, 2), True, 2),
    Car(Position(3, 3), False, 2),
    Car(Position(4, 0), False, 3),
    Car(Position(4, 4), True, 2)
], goal=Position(5, 2),
    board_height=6,
    board_width=6
)

game4 = Board(cars=[
    Car(length=2, horizontal=True, start=Position(1, 4)),
    Car(length=2, horizontal=False, start=Position(0, 0)),
    Car(length=3, horizontal=True, start=Position(1, 0)),
    Car(length=3, horizontal=False, start=Position(5, 0)),
    Car(length=3, horizontal=False, start=Position(3, 1)),
    Car(length=3, horizontal=True, start=Position(6, 1)),
    Car(length=3, horizontal=False, start=Position(8, 2)),
    Car(length=2, horizontal=True, start=Position(0, 3)),
    Car(length=3, horizontal=True, start=Position(5, 3)),
    Car(length=2, horizontal=False, start=Position(0, 4)),
    Car(length=2, horizontal=False, start=Position(3, 4)),
    Car(length=3, horizontal=False, start=Position(2, 5)),
    Car(length=3, horizontal=True, start=Position(5, 5)),
    Car(length=3, horizontal=False, start=Position(8, 5)),
    Car(length=2, horizontal=True, start=Position(0, 6)),
    Car(length=2, horizontal=False, start=Position(3, 6)),
    Car(length=2, horizontal=True, start=Position(4, 6)),
    Car(length=2, horizontal=False, start=Position(0, 7)),
    Car(length=2, horizontal=False, start=Position(4, 7)),
    Car(length=3, horizontal=True, start=Position(1, 8)),
    Car(length=2, horizontal=True, start=Position(5, 8)),
    Car(length=2, horizontal=True, start=Position(7, 8)),
], goal=Position(8, 4),
    board_height=9,
    board_width=9
)
