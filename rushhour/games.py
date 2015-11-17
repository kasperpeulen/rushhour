from rushhour.board import Board
from rushhour.car import Car
from rushhour.position import Position



game4 = Board(goal=(0, Position.new(8, 4)),
    board_height=9,
    board_width=9,
              cars=[
    Car(length=2, horizontal=True, start=Position.new(1, 4)),
    Car(length=2, horizontal=False, start=Position.new(0, 0)),
    Car(length=3, horizontal=True, start=Position.new(1, 0)),
    Car(length=3, horizontal=False, start=Position.new(5, 0)),
    Car(length=3, horizontal=False, start=Position.new(3, 1)),
    Car(length=3, horizontal=True, start=Position.new(6, 1)),
    Car(length=3, horizontal=False, start=Position.new(8, 2)),
    Car(length=2, horizontal=True, start=Position.new(0, 3)),
    Car(length=3, horizontal=True, start=Position.new(5, 3)),
    Car(length=2, horizontal=False, start=Position.new(0, 4)),
    Car(length=2, horizontal=False, start=Position.new(3, 4)),
    Car(length=3, horizontal=False, start=Position.new(2, 5)),
    Car(length=3, horizontal=True, start=Position.new(5, 5)),
    Car(length=3, horizontal=False, start=Position.new(8, 5)),
    Car(length=2, horizontal=True, start=Position.new(0, 6)),
    Car(length=2, horizontal=False, start=Position.new(3, 6)),
    Car(length=2, horizontal=True, start=Position.new(4, 6)),
    Car(length=2, horizontal=False, start=Position.new(0, 7)),
    Car(length=2, horizontal=False, start=Position.new(4, 7)),
    Car(length=3, horizontal=True, start=Position.new(1, 8)),
    Car(length=2, horizontal=True, start=Position.new(5, 8)),
    Car(length=2, horizontal=True, start=Position.new(7, 8)),
]
)


level1 = Board(cars=[
    Car(Position.new(2, 2), True, 2),
    Car(Position.new(3, 3), False, 2),
    Car(Position.new(4, 0), False, 3),
    Car(Position.new(4, 4), True, 2)
], goal=(0, Position.new(5, 2)),
    board_height=6,
    board_width=6
)


game2 = Board(goal=(0,Position.new(5, 2)),
    board_height=6,
    board_width=6,
    cars=[
    Car(length=2, horizontal=True, start=Position.new(2, 2)),
    Car(length=2, horizontal=True, start=Position.new(2, 0)),
    Car(length=2, horizontal=True, start=Position.new(4, 0)),
    Car(length=2, horizontal=True, start=Position.new(1, 1)),
    Car(length=2, horizontal=True, start=Position.new(3, 1)),
    Car(length=3, horizontal=False, start=Position.new(5, 1)),
    Car(length=2, horizontal=False, start=Position.new(4, 2)),
    Car(length=2, horizontal=True, start=Position.new(0, 3)),
    Car(length=2, horizontal=True, start=Position.new(2, 3)),
    Car(length=2, horizontal=False, start=Position.new(0, 4)),
    Car(length=2, horizontal=False, start=Position.new(3, 4)),
    Car(length=2, horizontal=True, start=Position.new(4, 4)),
    Car(length=2, horizontal=True, start=Position.new(4, 5)),
]
)

