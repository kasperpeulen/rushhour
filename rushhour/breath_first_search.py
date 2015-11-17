import time

from rushhour.board import Board, Win
from rushhour.car import Car
from rushhour.games import game2, level1, game4
# from rushhour.hash_table import states_checked_hash_table

def countPath(paths):
    count = 0
    for p in paths:
        count += len(p)
    return count

def breath_search(initial: Board):
    Car.boardWidth = initial.board_width
    Car.boardHeight = initial.board_height
    # initial board (stage 0)
    path = []
    path.append([initial])

    # states_checked_hash_table[hash(initial)] = [initial]
    print("step 0")
    print("new states:",1)
    print("total states:",countPath(path))
    print(initial)
    count = 0
    while True:
        nextPath = []
        for board in path[-1]:
            try:
                nextPath.extend(board.possible_next_boards())
            except Win:
                end = time.time()
                print(end - start)
                exit(0)

        count += 1

        print(time.time() - start)
        path.append(nextPath)
        print("step ", count)
        print("new states:",len(nextPath))
        print("total states:",countPath(path))

start = time.time()
breath_search(game2)

