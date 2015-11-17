import time

from rushhour.board import Board, Win
from rushhour.car import Car
from rushhour.games import game2, level1, game4
from rushhour.hash_table import states_checked_hash_table

def breath_search(initial: Board):
    Car.boardWidth = initial.board_width
    Car.boardHeight = initial.board_height
    # initial board (stage 0)
    path = []
    path.append([initial])
    print(initial)
    states_checked_hash_table[hash(initial)] = [initial]
    print("step 1")
    count = 1
    while True:
        nextPath = []
        for board in path[-1]:
            try:
                nextPath.extend(board.possible_next_boards())
            except Win:
                end = time.time()
                print(end - start)
                exit(0)
        print(len(nextPath))
        print(time.time() - start)
        count += 1
        print("step ", count)
        path.append(nextPath)

start = time.time()
breath_search(game2)
