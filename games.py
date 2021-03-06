from board import Board
from car import Car
from position import Position

level1 = Board(cars=[
    Car.new(Position.new(2, 2), True, 2),
    Car.new(Position.new(3, 3), False, 2),
    Car.new(Position.new(4, 0), False, 3),
    Car.new(Position.new(4, 4), True, 2)
], goal=(0, Position.new(5, 2)),
        board_height=6,
        board_width=6
)

game1 = Board(goal=(0, Position.new(5, 2)),
              board_height=6,
              board_width=6,
              cars=[
                  Car.new(length=2, horizontal=True, start=Position.new(3, 2)),
                  Car.new(length=3, horizontal=False, start=Position.new(2, 0)),
                  Car.new(length=2, horizontal=True, start=Position.new(3, 0)),
                  Car.new(length=3, horizontal=False, start=Position.new(5, 0)),
                  Car.new(length=2, horizontal=True, start=Position.new(4, 3)),
                  Car.new(length=2, horizontal=False, start=Position.new(0, 4)),
                  Car.new(length=2, horizontal=True, start=Position.new(1, 4)),
                  Car.new(length=2, horizontal=False, start=Position.new(3, 3)),
                  Car.new(length=2, horizontal=True, start=Position.new(4, 5)),
              ]
              )

game2 = Board(goal=(0, Position.new(5, 2)),
              board_height=6,
              board_width=6,
              cars=[
                  Car.new(length=2, horizontal=True, start=Position.new(2, 2)),
                  Car.new(length=2, horizontal=True, start=Position.new(2, 0)),
                  Car.new(length=2, horizontal=True, start=Position.new(4, 0)),
                  Car.new(length=2, horizontal=True, start=Position.new(1, 1)),
                  Car.new(length=2, horizontal=True, start=Position.new(3, 1)),
                  Car.new(length=3, horizontal=False, start=Position.new(5, 1)),
                  Car.new(length=2, horizontal=False, start=Position.new(4, 2)),
                  Car.new(length=2, horizontal=True, start=Position.new(0, 3)),
                  Car.new(length=2, horizontal=True, start=Position.new(2, 3)),
                  Car.new(length=2, horizontal=False, start=Position.new(0, 4)),
                  Car.new(length=2, horizontal=False, start=Position.new(3, 4)),
                  Car.new(length=2, horizontal=True, start=Position.new(4, 4)),
                  Car.new(length=2, horizontal=True, start=Position.new(4, 5)),
              ]
              )

game3 = Board(goal=(0, Position.new(5, 2)),
              board_height=6,
              board_width=6,
              cars=[
                  Car.new(length=2, horizontal=True, start=Position.new(0, 2)),
                  Car.new(length=2, horizontal=True, start=Position.new(1, 0)),
                  Car.new(length=3, horizontal=True, start=Position.new(3, 0)),
                  Car.new(length=2, horizontal=True, start=Position.new(1, 1)),
                  Car.new(length=2, horizontal=False, start=Position.new(3, 1)),
                  Car.new(length=2, horizontal=True, start=Position.new(4, 1)),
                  Car.new(length=2, horizontal=False, start=Position.new(2, 2)),
                  Car.new(length=2, horizontal=False, start=Position.new(5, 2)),
                  Car.new(length=2, horizontal=True, start=Position.new(0, 3)),
                  Car.new(length=2, horizontal=True, start=Position.new(3, 3)),
                  Car.new(length=2, horizontal=False, start=Position.new(0, 4)),
                  Car.new(length=2, horizontal=False, start=Position.new(2, 4)),
                  Car.new(length=2, horizontal=True, start=Position.new(4, 4)),
              ]
              )

game4 = Board(goal=(0, Position.new(8, 4)),
              board_height=9,
              board_width=9,
              cars=[
                  Car.new(length=2, horizontal=True, start=Position.new(1, 4)),
                  Car.new(length=2, horizontal=False, start=Position.new(0, 0)),
                  Car.new(length=3, horizontal=True, start=Position.new(1, 0)),
                  Car.new(length=3, horizontal=False, start=Position.new(5, 0)),
                  Car.new(length=3, horizontal=False, start=Position.new(3, 1)),
                  Car.new(length=3, horizontal=True, start=Position.new(6, 1)),
                  Car.new(length=3, horizontal=False, start=Position.new(8, 2)),
                  Car.new(length=2, horizontal=True, start=Position.new(0, 3)),
                  Car.new(length=3, horizontal=True, start=Position.new(5, 3)),
                  Car.new(length=2, horizontal=False, start=Position.new(0, 4)),
                  Car.new(length=2, horizontal=False, start=Position.new(3, 4)),
                  Car.new(length=3, horizontal=False, start=Position.new(2, 5)),
                  Car.new(length=3, horizontal=True, start=Position.new(5, 5)),
                  Car.new(length=3, horizontal=False, start=Position.new(8, 5)),
                  Car.new(length=2, horizontal=True, start=Position.new(0, 6)),
                  Car.new(length=2, horizontal=False, start=Position.new(3, 6)),
                  Car.new(length=2, horizontal=True, start=Position.new(4, 6)),
                  Car.new(length=2, horizontal=False, start=Position.new(0, 7)),
                  Car.new(length=2, horizontal=False, start=Position.new(4, 7)),
                  Car.new(length=3, horizontal=True, start=Position.new(1, 8)),
                  Car.new(length=2, horizontal=True, start=Position.new(5, 8)),
                  Car.new(length=2, horizontal=True, start=Position.new(7, 8)),
              ]
              )

game5 = Board(goal=(0, Position.new(8, 4)),
              board_height=9,
              board_width=9,
              cars=[
                  Car.new(length=2, horizontal=True, start=Position.new(6, 4)),
                  Car.new(length=3, horizontal=True, start=Position.new(0, 0)),
                  Car.new(length=3, horizontal=False, start=Position.new(3, 0)),
                  Car.new(length=2, horizontal=False, start=Position.new(5, 0)),
                  Car.new(length=2, horizontal=False, start=Position.new(6, 0)),
                  Car.new(length=2, horizontal=True, start=Position.new(7, 1)),
                  Car.new(length=2, horizontal=True, start=Position.new(4, 2)),
                  Car.new(length=2, horizontal=False, start=Position.new(6, 2)),
                  Car.new(length=2, horizontal=True, start=Position.new(4, 3)),
                  Car.new(length=2, horizontal=True, start=Position.new(7, 3)),
                  Car.new(length=3, horizontal=True, start=Position.new(2, 4)),
                  Car.new(length=3, horizontal=False, start=Position.new(5, 4)),
                  Car.new(length=3, horizontal=False, start=Position.new(8, 4)),
                  Car.new(length=2, horizontal=False, start=Position.new(0, 5)),
                  Car.new(length=2, horizontal=False, start=Position.new(2, 5)),
                  Car.new(length=2, horizontal=True, start=Position.new(3, 6)),
                  Car.new(length=2, horizontal=True, start=Position.new(6, 6)),
                  Car.new(length=2, horizontal=False, start=Position.new(0, 7)),
                  Car.new(length=2, horizontal=False, start=Position.new(1, 7)),
                  Car.new(length=2, horizontal=True, start=Position.new(2, 7)),
                  Car.new(length=2, horizontal=True, start=Position.new(2, 8)),
                  Car.new(length=2, horizontal=False, start=Position.new(4, 7)),
                  Car.new(length=3, horizontal=True, start=Position.new(5, 7)),
                  Car.new(length=2, horizontal=False, start=Position.new(8, 7)),
              ]
              )

game6 = Board(goal=(0, Position.new(8, 4)),
              board_height=9,
              board_width=9,
              cars=[
                  Car.new(length=2, horizontal=True, start=Position.new(0, 4)),
                  Car.new(length=2, horizontal=True, start=Position.new(0, 0)),
                  Car.new(length=2, horizontal=True, start=Position.new(2, 0)),
                  Car.new(length=2, horizontal=False, start=Position.new(4, 0)),
                  Car.new(length=2, horizontal=False, start=Position.new(7, 0)),
                  Car.new(length=2, horizontal=False, start=Position.new(0, 1)),
                  Car.new(length=3, horizontal=True, start=Position.new(1, 1)),
                  Car.new(length=2, horizontal=True, start=Position.new(5, 1)),
                  Car.new(length=2, horizontal=True, start=Position.new(2, 2)),
                  Car.new(length=2, horizontal=True, start=Position.new(7, 2)),
                  Car.new(length=2, horizontal=False, start=Position.new(4, 2)),
                  Car.new(length=2, horizontal=False, start=Position.new(5, 2)),
                  Car.new(length=2, horizontal=False, start=Position.new(2, 3)),
                  Car.new(length=3, horizontal=False, start=Position.new(3, 3)),
                  Car.new(length=3, horizontal=True, start=Position.new(6, 3)),
                  Car.new(length=2, horizontal=False, start=Position.new(1, 5)),
                  Car.new(length=2, horizontal=True, start=Position.new(4, 5)),
                  Car.new(length=2, horizontal=True, start=Position.new(6, 5)),
                  Car.new(length=3, horizontal=False, start=Position.new(8, 5)),
                  Car.new(length=3, horizontal=False, start=Position.new(0, 6)),
                  Car.new(length=2, horizontal=True, start=Position.new(2, 6)),
                  Car.new(length=2, horizontal=True, start=Position.new(2, 7)),
                  Car.new(length=3, horizontal=True, start=Position.new(1, 8)),
                  Car.new(length=3, horizontal=False, start=Position.new(4, 6)),
                  Car.new(length=3, horizontal=True, start=Position.new(5, 6)),
                  Car.new(length=2, horizontal=True, start=Position.new(5, 7)),
              ]
              )

game7 = Board(
        goal=(0, Position.new(11, 5)),
        board_height=12,
        board_width=12,
        cars=[
            Car.new(length=2, horizontal=True, start=Position.new(2, 5)),
            Car.new(length=2, horizontal=False, start=Position.new(0, 0)),
            Car.new(length=3, horizontal=True, start=Position.new(0, 2)),
            Car.new(length=3, horizontal=False, start=Position.new(0, 3)),
            Car.new(length=3, horizontal=True, start=Position.new(0, 6)),
            Car.new(length=3, horizontal=True, start=Position.new(0, 7)),
            Car.new(length=2, horizontal=True, start=Position.new(0, 8)),
            Car.new(length=3, horizontal=False, start=Position.new(1, 3)),
            Car.new(length=2, horizontal=True, start=Position.new(1, 11)),
            Car.new(length=3, horizontal=True, start=Position.new(2, 4)),
            Car.new(length=2, horizontal=False, start=Position.new(2, 8)),
            Car.new(length=2, horizontal=True, start=Position.new(3, 2)),
            Car.new(length=2, horizontal=False, start=Position.new(3, 6)),
            Car.new(length=3, horizontal=True, start=Position.new(3, 8)),
            Car.new(length=3, horizontal=True, start=Position.new(3, 9)),
            Car.new(length=3, horizontal=True, start=Position.new(3, 11)),
            Car.new(length=2, horizontal=False, start=Position.new(4, 5)),
            Car.new(length=2, horizontal=True, start=Position.new(4, 7)),
            Car.new(length=2, horizontal=False, start=Position.new(5, 1)),
            Car.new(length=2, horizontal=False, start=Position.new(5, 3)),
            Car.new(length=2, horizontal=False, start=Position.new(5, 5)),
            Car.new(length=2, horizontal=False, start=Position.new(6, 0)),
            Car.new(length=3, horizontal=False, start=Position.new(6, 2)),
            Car.new(length=3, horizontal=False, start=Position.new(6, 6)),
            Car.new(length=3, horizontal=False, start=Position.new(6, 9)),
            Car.new(length=3, horizontal=True, start=Position.new(7, 0)),
            Car.new(length=2, horizontal=True, start=Position.new(7, 2)),
            Car.new(length=2, horizontal=True, start=Position.new(7, 3)),
            Car.new(length=3, horizontal=True, start=Position.new(7, 4)),
            Car.new(length=2, horizontal=False, start=Position.new(7, 6)),
            Car.new(length=3, horizontal=True, start=Position.new(7, 8)),
            Car.new(length=2, horizontal=True, start=Position.new(7, 11)),
            Car.new(length=2, horizontal=True, start=Position.new(8, 9)),
            Car.new(length=2, horizontal=True, start=Position.new(9, 3)),
            Car.new(length=2, horizontal=False, start=Position.new(9, 6)),
            Car.new(length=2, horizontal=False, start=Position.new(9, 10)),
            Car.new(length=2, horizontal=True, start=Position.new(10, 0)),
            Car.new(length=2, horizontal=False, start=Position.new(10, 1)),
            Car.new(length=2, horizontal=True, start=Position.new(10, 6)),
            Car.new(length=2, horizontal=True, start=Position.new(10, 7)),
            Car.new(length=3, horizontal=False, start=Position.new(10, 9)),
            Car.new(length=2, horizontal=False, start=Position.new(11, 1)),
            Car.new(length=2, horizontal=False, start=Position.new(11, 8)),
            Car.new(length=2, horizontal=False, start=Position.new(11, 10)),
        ])

games = [game1, game2, game3, game4, game5, game6, game7]
