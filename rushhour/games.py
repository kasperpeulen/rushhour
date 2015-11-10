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

print(game2)
